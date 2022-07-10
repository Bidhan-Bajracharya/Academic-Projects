/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Coursework;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author lenovo
 */
public class ImportAndExport {
    public static void importFile(JTable table){
        FileReader fr = null;
        String filepath = "src\\Coursework\\data.txt";
        File file = new File(filepath);
        try {
            fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            DefaultTableModel model = (DefaultTableModel)table.getModel();
            Object[] lines = br.lines().toArray();
            for (int i = 0; i < lines.length; i++){
                String [] row = lines [i].toString().split(",");
                model.addRow(row);
            }
        } catch (FileNotFoundException ex) {
            java.util.logging.Logger.getLogger(AirlineInfo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
    }
    
    public static void exportFile(JTable table){
        String filepath = "src\\Coursework\\data.txt";
        File file = new File(filepath);
        try {
            FileWriter fw = new FileWriter(file);
            BufferedWriter bw = new BufferedWriter(fw);
            for (int i = 0;i<table.getRowCount();i++)
            {
                for(int j=0;j<table.getColumnCount();j++)
                {
                    bw.write(table.getValueAt(i, j).toString() + ",");
                }
                bw.newLine();
            }
            bw.close();
            fw.close();
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(AirlineInfo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
    }
}
