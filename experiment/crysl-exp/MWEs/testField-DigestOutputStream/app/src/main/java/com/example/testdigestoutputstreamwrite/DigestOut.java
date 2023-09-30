package com.example.testdigestoutputstreamwrite;

import android.util.Log;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.DigestOutputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class DigestOut {

    protected final DigestOutputStream digestOutputStream;

    protected DigestOut() throws NoSuchAlgorithmException {
        // initialize a digestOutputStream object in this class construct function
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        ByteArrayOutputStream dst = new ByteArrayOutputStream();
        digestOutputStream = new DigestOutputStream(dst, md);
    }

    public void writeChecksum(byte[] bytes) throws IOException {
        // call write method of digestOutputStream object
        digestOutputStream.write(bytes);
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