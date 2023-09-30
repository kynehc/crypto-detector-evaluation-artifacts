package com.example.testkeystoredefuse;

import java.io.File;
import java.io.InputStream;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.SecureRandom;

public class KeyStoreBuilder {
    private File keyStoreFile;
    private String password;

    KeyStore loadAppKeyStore() throws Exception {
        KeyStore ks;

        genPassword();
        ks = KeyStore.getInstance(KeyStore.getDefaultType());
        InputStream is = new java.io.FileInputStream(keyStoreFile);

        ks.load(is, password.toCharArray());

        return ks;
    }

    public void genPassword() {
        byte[] pass = new byte[64];
        SecureRandom secureRandom = new SecureRandom();
        secureRandom.nextBytes(pass);
        password = bytesToHex(pass);
    }

    // to convert bytes to hex string
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
