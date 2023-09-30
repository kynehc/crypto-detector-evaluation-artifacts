package com.example.testnevertypeoftochararray;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.net.PasswordAuthentication;
import java.security.SecureRandom;

public class MainActivity extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // use SecureRandom to get a random char array for password
        SecureRandom secureRan = new SecureRandom();
        byte bytes[] = new byte[128];
        secureRan.nextBytes(bytes);
        char[] password = new String(bytes).toCharArray();

        // call PasswordAuthentication with randomized char array as password
        String userName = "user";
        try {
            PasswordAuthentication passwordAuthentication = new PasswordAuthentication(userName, password);
            char[] pass = passwordAuthentication.getPassword();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}