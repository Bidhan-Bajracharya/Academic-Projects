/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Coursework;

import javax.swing.JTextField;

/**
 *
 * @author lenovo
 */
public class TextFieldRestriction {
    
    private static boolean containsSpecialChars(char c){  
        // checking for special characters
        String specialCharactersString = "!@#$%&*()'+,-./:;<=>?[]^_`{|}";
        if(specialCharactersString.contains(Character.toString(c))){
            return true;
        }
        return false;
    }
    
    public static void onlyDigitTextFields(JTextField tf, java.awt.event.KeyEvent evt){
        // method that only allows digits
        char cc = evt.getKeyChar();
        if(Character.isDigit(cc)||(cc == evt.VK_BACK_SPACE)||(cc == evt.VK_DELETE)){
            tf.setEditable(true);
        }else{
            tf.setEditable(false);
        }
    }
    
    public static void onlyCharTextFields(JTextField tf, java.awt.event.KeyEvent evt){
        // method that doesn't allow any digit and special characters
        char cc = evt.getKeyChar();
        if(!containsSpecialChars(cc)){
            if(!Character.isDigit(cc)||(cc == evt.VK_BACK_SPACE)||(cc == evt.VK_DELETE)){
                tf.setEditable(true);
            }
            else{
                tf.setEditable(false);
            }
        }
        else{
            tf.setEditable(false);
        }
    } 
    
    public static void bothCharAndDigitTextFields(JTextField tf, java.awt.event.KeyEvent evt){
        // method that doesn't allow only special characters
        char cc = evt.getKeyChar();
        if(!containsSpecialChars(cc) && cc != evt.VK_SPACE){
            tf.setEditable(true);
        }
        else{
            tf.setEditable(false);
        }
    }
}
