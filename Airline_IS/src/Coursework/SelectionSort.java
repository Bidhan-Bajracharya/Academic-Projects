/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Coursework;

import java.util.ArrayList;

/**
 *
 * @author lenovo
 */
public class SelectionSort {
    public static void sort(ArrayList<String> al) {
        // sorting based on price
        for (int i = 6; i < al.size(); i = i + 7) {
            int currentMinIndex = i;
            for (int j = i + 7; j < al.size(); j = j + 7) {
                String min = al.get(currentMinIndex);
                int minPos = Integer.parseInt(min);
                if (minPos > Integer.parseInt(al.get(j))) {
                    currentMinIndex = j;
                }
            }
            
            if (currentMinIndex != i) {
                // sorting each column's data respective to its price
                String priceTemp =  al.get(i);
                al.set(i, al.get(currentMinIndex));
                al.set(currentMinIndex, priceTemp);

                String airlineTemp = al.get(i - 1);
                al.set(i - 1, al.get(currentMinIndex-1));
                al.set(currentMinIndex - 1, airlineTemp);

                String gateTemp = al.get(i - 2);
                al.set(i - 2, al.get(currentMinIndex-2));
                al.set(currentMinIndex - 2, gateTemp);
                
                String statusTemp = al.get(i - 3);
                al.set(i - 3, al.get(currentMinIndex-3));
                al.set(currentMinIndex - 3, statusTemp);
                
                String timeTemp = al.get(i - 4);
                al.set(i - 4, al.get(currentMinIndex-4));
                al.set(currentMinIndex - 4, timeTemp);
                
                String destinationTemp = al.get(i - 5);
                al.set(i - 5, al.get(currentMinIndex-5));
                al.set(currentMinIndex - 5, destinationTemp);
                
                String flightTemp = al.get(i - 6);
                al.set(i - 6, al.get(currentMinIndex-6));
                al.set(currentMinIndex - 6, flightTemp);
            }
        }
    }
}
