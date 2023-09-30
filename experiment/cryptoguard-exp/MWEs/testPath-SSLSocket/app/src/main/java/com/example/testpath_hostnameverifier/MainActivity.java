package com.example.testpath_hostnameverifier;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLHandshakeException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TestClass test = new TestClass();
        try {
            test.test();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}