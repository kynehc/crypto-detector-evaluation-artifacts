package com.example.testdigestoutputstreamwrite;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.DigestOutputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // some data to be digest
        String data = "abcdefghijklmnopqrstuvxyz";
        // initialize a DigestOut class object and call writeChecksum
        try {
            DigestOut digestOut = new DigestOut();
            digestOut.writeChecksum(data.getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}