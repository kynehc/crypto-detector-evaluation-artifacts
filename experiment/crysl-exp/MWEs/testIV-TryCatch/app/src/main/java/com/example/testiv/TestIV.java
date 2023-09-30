package com.example.testiv;

import android.util.Log;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.SecureRandom;

import javax.crypto.spec.IvParameterSpec;

public class TestIV {

    private final SecureRandom random;

    public TestIV() {
        random = new SecureRandom() ;
    }

    public void test() throws IOException {
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        byte[] initializationVector = new byte[16];
        random.nextBytes(initializationVector);

        output.write(initializationVector);
        IvParameterSpec ivParameterSpec = new IvParameterSpec(initializationVector);
        Log.e("Test", bytesToHex(initializationVector));
    }

    // to convert bytes to hex string for output
    private static final char[] HEX_ARRAY = "0123456789ABCDEF".toCharArray();
    public static String bytesToHex(byte[] bytes) {
        char[] hexChars = new char[bytes.length * 2];
        for (int j = 0; j < bytes.length; j++) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = HEX_ARRAY[v >>> 4];
            hexChars[j * 2 + 1] = HEX_ARRAY[v & 0x0F];
        }
        return new String(hexChars);
    }
}
