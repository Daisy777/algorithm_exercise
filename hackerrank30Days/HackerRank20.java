import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }

        // Write Your Code Here
        int swapcnt = 0;
        for (int i=0; i<a.length; i++) {
            for (int j=a.length-1; j>i; j--) {
                if (a[j] < a[j-1]) {
                    swap(a, j-1, j);
                    swapcnt ++;
                }
            }
        }

        // print the required result
        System.out.printf("Array is sorted in %d swaps.\n", swapcnt);
        System.out.printf("First Element: %d\n", a[0]);
        System.out.printf("Last Element: %d\n", a[a.length-1]);
    }

    public static void swap(int[] arr, int l1, int l2) {
        int temp = arr[l1];
        arr[l1] = arr[l2];
        arr[l2] = temp;
    }
}

