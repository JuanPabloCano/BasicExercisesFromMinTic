/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.*;
/**
 *
 * @author Usuario
 */
public class ConexionBD {
    
    public Connection conexion;
    public Statement sentencia;
    public ResultSet resultado;
    
    public void conectarBD(){
        try{
            final String Controlador= "com.mysql.cj.jdbc.Driver";
            Class.forName(Controlador);
            final String url_bd= "jdbc:mysql://localhost:3306/registro";
            conexion= DriverManager.getConnection(url_bd, "root", "NBAjordan23@");
            sentencia= conexion.createStatement();
            
        }catch (ClassNotFoundException | SQLException ex){
            JOptionPane.showMessageDialog(null, ex.getMessage(), "ERROR", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    public void DesconectarBD(){
        try{
            if (conexion != null){
                if (sentencia != null){
                    sentencia.close();
                }
                conexion.close();
            }
        }catch (SQLException ex){
            JOptionPane.showMessageDialog(null, ex.getMessage(), "ERROR", JOptionPane.ERROR_MESSAGE);
            System.exit(1);
        }
    }
    
    public Connection getConnection(){
        return conexion;
    }
}
