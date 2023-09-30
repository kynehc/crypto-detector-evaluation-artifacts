package com.example.testpbeparameterspec;

import android.util.Log;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import javax.crypto.spec.PBEParameterSpec;

public class CryptoHelper {
    private static byte[] salt = null;
    private static String TAG = "CryptoHelper";
    private static PBEParameterSpec pbeParamSpec;

    // set salt and initialize PBEParameterSpec
    public void init(byte[] salt2) {
        setSalt(salt2);
        pbeParamSpec = new PBEParameterSpec(salt, 10000);
    }

    // to set salt
    private void setSalt(byte[] saltIn) {
        byte[] byteSaltIn = saltIn;
        salt = byteSaltIn;
        Log.e(TAG, toHexString(salt));
    }

    // SecureRandom to generate salt
    public static byte[] generateSalt() throws NoSuchAlgorithmException {
        byte[] salt2 = new byte[16];
        try {
            SecureRandom.getInstance("SHA1PRNG").nextBytes(salt2);
            Log.e(TAG, toHexString(salt2));
            return salt2;
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            throw e;
        }
    }

    public static String toHexString(byte[] bytes) {
        StringBuffer retString = new StringBuffer();
        for (byte b : bytes) {
            retString.append(Integer.toHexString((b & 255) + 256).substring(1));
        }
        return retString.toString();
    }
}
