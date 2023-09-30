package com.example.testiv;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import java.io.IOException;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TestIV instance = new TestIV();

        try {
            instance.test();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}