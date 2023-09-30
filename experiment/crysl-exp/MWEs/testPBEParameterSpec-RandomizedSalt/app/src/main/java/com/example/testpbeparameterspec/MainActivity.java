package com.example.testpbeparameterspec;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import javax.crypto.spec.PBEParameterSpec;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CryptoHelper cryptoHelper = new CryptoHelper();
        try {
            byte[] salt = CryptoHelper.generateSalt();
            Log.e("Main", CryptoHelper.toHexString(salt));
            cryptoHelper.init(salt);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}