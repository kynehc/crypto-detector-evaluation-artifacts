package com.example.testmap_iv;

import java.security.SecureRandom;
import java.util.HashMap;
import java.util.Map;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

public class testIV {
    Map<String, byte[]> IVmap = new HashMap<String, byte[]>();

    public String encrypt(String data, byte[] rawiv) {
        try {
            KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
            keyGenerator.init(256);
            SecretKey secretKey = keyGenerator.generateKey();
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            byte[] initialisationVector = rawiv;
            IvParameterSpec iv = new IvParameterSpec(initialisationVector);
            cipher.init(Cipher.ENCRYPT_MODE, secretKey, iv);
            return new String(cipher.doFinal(data.getBytes()));
        } catch (Exception e){
            e.printStackTrace();
            return data;
        }
    }

    public String getIvEncrypt(String data, String name){
        byte[] rawiv = IVmap.get(name);
        return encrypt(data, rawiv);
    }

    public String encryptWrapper(String data){
        byte[] iv = new byte[16];
        SecureRandom sr = new SecureRandom();
        sr.nextBytes(iv);
        IVmap.put("IV", iv);
        return getIvEncrypt(data, "IV");
    }
}