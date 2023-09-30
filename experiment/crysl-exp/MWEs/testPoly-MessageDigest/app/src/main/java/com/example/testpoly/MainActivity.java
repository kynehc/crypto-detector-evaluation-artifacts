package com.example.testpoly;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        UpdateKey akey = new UpdateKey();
        KeyGen keygen = new KeyGen();
        keygen.getKey(akey);
    }
}