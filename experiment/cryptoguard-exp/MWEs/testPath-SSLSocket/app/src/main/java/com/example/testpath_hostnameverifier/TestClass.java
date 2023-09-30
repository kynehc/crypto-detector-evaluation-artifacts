package com.example.testpath_hostnameverifier;

import java.security.SecureRandom;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLHandshakeException;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.TrustManagerFactory;

public class TestClass {
    public void test() throws Exception {
        SSLContext sslCtx = SSLContext.getInstance("TLS");
        TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        sslCtx.init(null, tmf.getTrustManagers(), new SecureRandom());
        SSLSocket socket = (SSLSocket) sslCtx.getSocketFactory().createSocket("xxx.com",443);

        HostnameVerifier hostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();
        if (hostnameVerifier != null && !hostnameVerifier.verify("gmail.com", socket.getSession())) {
            throw new SSLHandshakeException("Hostname doesn't match certificate");
        }
    }
}
