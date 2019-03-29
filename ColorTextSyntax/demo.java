import java.util.*;
import java.util.Scanner;
public class Hello {
    public static void main(String[] args) {
      System.out.println("Hello, World");
    }
    public void random_method() {
      //example taken from oracle.com
      int testscore = 76;
        char grade;

        if (testscore >= 90) {
            grade = 'A';
        } else if (testscore >= 80) {
            grade = 'B';
        } else if (testscore >= 70) {
            grade = 'C';
        } else if (testscore >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }

        while(True) {
          System.out.println("monkaS");
        }
        System.out.println("Grade = " + grade);

        try {
         System.out.println("try");
       }
       catch (ArithmeticException e) {
         System.out.println("catch");
      }
    }
  }
