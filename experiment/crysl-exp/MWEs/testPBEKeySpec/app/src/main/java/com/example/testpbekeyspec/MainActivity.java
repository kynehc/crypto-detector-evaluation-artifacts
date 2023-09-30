package com.example.testpbekeyspec;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import java.security.SecureRandom;

import javax.crypto.SecretKeyFactory;
import javax.crypto.interfaces.PBEKey;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // use SecureRandom to generate password and salt byte arrays
        byte[] pass = new byte[256];
        byte[] salt = new byte[256];
        SecureRandom secureRandom = new SecureRandom();
        secureRandom.nextBytes(pass);
        secureRandom.nextBytes(salt);

        byte[] key = getKey(pass, salt, 10000, 256);
    }

    public byte[] getKey(byte[] _pass, byte[] salt, int iterations, int size) {
        // convert byte array to char array
        char[] pass = new char[_pass.length];
        for(int i=0; i < _pass.length; i++){
            pass[i] = (char) (_pass[i]&0xff);
        }

        // generate a key via a PBEKeySpec
        try{
            PBEKeySpec spec = new PBEKeySpec(pass, salt, iterations, size*8); // size*8 bits for key length
            SecretKeyFactory skf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
            byte[] key = skf.generateSecret(spec).getEncoded();
            return key;
        } catch (Exception e) {
        }
        return null;
    }

}