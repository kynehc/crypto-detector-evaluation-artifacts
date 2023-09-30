package com.example.testalgoparam;


import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;

import java.io.UnsupportedEncodingException;
import java.security.AlgorithmParameters;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;


public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // do a correct AES encryption
        try {
            byte[] somedata = "abcdefghijklmnopqrstuvxyz".getBytes("UTF-8");

            // to generate a key for AES encryption
            KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
            keyGenerator.init(256);
            SecretKey secretKey = keyGenerator.generateKey();

            // get a Cipher object to do AES encryption
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            AlgorithmParameters params = cipher.getParameters();

            Log.d("test", new String(params.getEncoded(), "UTF-8"));

            byte[] ciphertext = cipher.doFinal(somedata);

            // get AlgorithmParameters object from cipher object
            // byte[] encodedAlgParams = params.getEncoded();
            byte[] iv= params.getParameterSpec(IvParameterSpec.class).getIV();

            // init another algoParam from above AlgorithmParameters
            AlgorithmParameters algoParam = AlgorithmParameters.getInstance("AES");
            // algoParam.init(new IvParameterSpec(encodedAlgParams));
            algoParam.init(new IvParameterSpec(iv));

            // get another cipher of AES to decrypt
            Cipher decryptCipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            decryptCipher.init(Cipher.DECRYPT_MODE, secretKey, algoParam);
            byte[] plaintext = decryptCipher.doFinal(ciphertext);

            Log.d("test", new String(plaintext, "UTF-8"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}