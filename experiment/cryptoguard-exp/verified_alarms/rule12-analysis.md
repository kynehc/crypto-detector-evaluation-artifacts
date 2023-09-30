Rule: 12 Should check HostnameVerification manually

------------------------------------------------
```
#1
Class: org.apache.http.impl.pool.BasicConnFactory
Method: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)
Apk Num:13

Apk:eu.devunit.fb_client_4.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:org.smssecure.smssecure_145.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:de.live.gdev.cherrymusic_14.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:eu.e43.impeller_9052.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:com.willhauck.linconnectclient_221.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:com.jbirdvegas.mgerrit_2111084.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:de.live.gdev.timetracker_26.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:com.yassirh.digitalocean_32.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:org.midorinext.android_36.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:de.geeksfactory.opacclient_232.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:theakki.synctool_100.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:com.lgallardo.qbittorrentclientpro_390.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Apk:eu.veldsoft.complica4_4.apk
Err: Didn't manually verify hostname in create in <org.apache.http.impl.pool.BasicConnFactory: org.apache.http.HttpClientConnection create(org.apache.http.HttpHost)>::create.

Misuse Num:13
```

TP

------------------------------------------------
```
#2
Class: org.apache.commons.net.smtp.SMTPSClient
Method: void performSSLNegotiation()
Apk Num:12

Apk:io.github.ismywebsiteup_11.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.gianlu.aria2app_221.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:fr.gouv.etalab.mastodon_383.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.mendhak.gpslogger_120.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:li.klass.fhem_141.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:org.courville.nova_404911.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.rfo.basic_500.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:ca.rmen.android.networkmonitor_13200.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.gs.mobileprint_1.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:app.fedilab.lite_383.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.rfo.LASKmobile_501.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:org.fdroid.nearby_2.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.smtp.SMTPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Misuse Num:12
```

FP: Forward slicing only take the slicing result of final statement in the graph of a method. However, the taken branch is an additinal null check ` if (hostnameVerifier != null && ... )` and will result in a slicing result without containing `hostnameVerifier.verify(hostAddress, sSLSocket.getSession())`.

Source code snippet:
```
private void performSSLNegotiation() throws IOException {
        initSSLContext();
        SSLSocketFactory socketFactory = this.context.getSocketFactory();
        String hostAddress = this._hostname_ != null ? this._hostname_ : getRemoteAddress().getHostAddress();
        SSLSocket sSLSocket = (SSLSocket) socketFactory.createSocket(this._socket_, hostAddress, getRemotePort(), true);
        sSLSocket.setEnableSessionCreation(true);
        sSLSocket.setUseClientMode(true);
        if (this.tlsEndpointChecking) {
            SSLSocketUtils.enableEndpointNameVerification(sSLSocket);
        }
        String[] strArr = this.protocols;
        if (strArr != null) {
            sSLSocket.setEnabledProtocols(strArr);
        }
        String[] strArr2 = this.suites;
        if (strArr2 != null) {
            sSLSocket.setEnabledCipherSuites(strArr2);
        }
        sSLSocket.startHandshake();
        this._socket_ = sSLSocket;
        this._input_ = sSLSocket.getInputStream();
        this._output_ = sSLSocket.getOutputStream();
        this._reader = new CRLFLineReader(new InputStreamReader(this._input_, this.encoding));
        this._writer = new BufferedWriter(new OutputStreamWriter(this._output_, this.encoding));
        HostnameVerifier hostnameVerifier = this.hostnameVerifier;
        if (hostnameVerifier != null && !hostnameVerifier.verify(hostAddress, sSLSocket.getSession())) {
            throw new SSLHandshakeException("Hostname doesn't match certificate");
        }
    }
```


------------------------------------------------
```
#3
Class: org.apache.commons.net.ftp.FTPSClient
Method: void sslNegotiation()
Apk Num:12

Apk:io.github.ismywebsiteup_11.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:org.brandroid.openmanager_212.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:fr.gouv.etalab.mastodon_383.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:com.mendhak.gpslogger_120.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:li.klass.fhem_141.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:org.courville.nova_404911.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:com.rfo.basic_500.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:com.gs.mobileprint_1.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:app.fedilab.lite_383.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:com.rfo.LASKmobile_501.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:com.dngames.mobilewebcam_118.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Apk:org.fdroid.nearby_2.apk
Err: Didn't manually verify hostname in sslNegotiation in <org.apache.commons.net.ftp.FTPSClient: void sslNegotiation()>::sslNegotiation.

Misuse Num:12
```

FP: Forward slicing only take the slicing result of final statement in the graph of a method. However, the taken branch is an additinal null check ` if (hostnameVerifier != null && ... )` and will result in a slicing result without containing `hostnameVerifier.verify(hostAddress, sSLSocket.getSession())`.

Source code snippet:
```
    protected void sslNegotiation() throws IOException {
        HostnameVerifier hostnameVerifier;
        this.plainSocket = this._socket_;
        initSslContext();
        SSLSocketFactory socketFactory = this.context.getSocketFactory();
        String hostAddress = this._hostname_ != null ? this._hostname_ : getRemoteAddress().getHostAddress();
        SSLSocket sSLSocket = (SSLSocket) socketFactory.createSocket(this._socket_, hostAddress, this._socket_.getPort(), false);
        sSLSocket.setEnableSessionCreation(this.isCreation);
        sSLSocket.setUseClientMode(this.isClientMode);
        if (this.isClientMode) {
            if (this.tlsEndpointChecking) {
                SSLSocketUtils.enableEndpointNameVerification(sSLSocket);
            }
        } else {
            sSLSocket.setNeedClientAuth(this.isNeedClientAuth);
            sSLSocket.setWantClientAuth(this.isWantClientAuth);
        }
        String[] strArr = this.protocols;
        if (strArr != null) {
            sSLSocket.setEnabledProtocols(strArr);
        }
        String[] strArr2 = this.suites;
        if (strArr2 != null) {
            sSLSocket.setEnabledCipherSuites(strArr2);
        }
        sSLSocket.startHandshake();
        this._socket_ = sSLSocket;
        this._controlInput_ = new BufferedReader(new InputStreamReader(sSLSocket.getInputStream(), getControlEncoding()));
        this._controlOutput_ = new BufferedWriter(new OutputStreamWriter(sSLSocket.getOutputStream(), getControlEncoding()));
        if (this.isClientMode && (hostnameVerifier = this.hostnameVerifier) != null && !hostnameVerifier.verify(hostAddress, sSLSocket.getSession())) {
            throw new SSLHandshakeException("Hostname doesn't match certificate");
        }
    }
```

------------------------------------------------
```
#4
Class: org.apache.commons.net.pop3.POP3SClient
Method: void performSSLNegotiation()
Apk Num:10

Apk:io.github.ismywebsiteup_11.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.gianlu.aria2app_221.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:fr.gouv.etalab.mastodon_383.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:li.klass.fhem_141.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:org.courville.nova_404911.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.rfo.basic_500.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.gs.mobileprint_1.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:app.fedilab.lite_383.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.rfo.LASKmobile_501.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:org.fdroid.nearby_2.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.pop3.POP3SClient: void performSSLNegotiation()>::performSSLNegotiation.

Misuse Num:10
```

FP: Forward slicing only take the slicing result of final statement in the graph of a method. However, the taken branch is an additinal null check ` if (hostnameVerifier != null && ... )` and will result in a slicing result without containing `hostnameVerifier.verify(hostAddress, sSLSocket.getSession())`.

Source code snippet:
```
private void performSSLNegotiation() throws IOException {
        initSSLContext();
        SSLSocketFactory socketFactory = this.context.getSocketFactory();
        String hostAddress = this._hostname_ != null ? this._hostname_ : getRemoteAddress().getHostAddress();
        SSLSocket sSLSocket = (SSLSocket) socketFactory.createSocket(this._socket_, hostAddress, getRemotePort(), true);
        sSLSocket.setEnableSessionCreation(true);
        sSLSocket.setUseClientMode(true);
        if (this.tlsEndpointChecking) {
            SSLSocketUtils.enableEndpointNameVerification(sSLSocket);
        }
        String[] strArr = this.protocols;
        if (strArr != null) {
            sSLSocket.setEnabledProtocols(strArr);
        }
        String[] strArr2 = this.suites;
        if (strArr2 != null) {
            sSLSocket.setEnabledCipherSuites(strArr2);
        }
        sSLSocket.startHandshake();
        this._socket_ = sSLSocket;
        this._input_ = sSLSocket.getInputStream();
        this._output_ = sSLSocket.getOutputStream();
        this._reader = new CRLFLineReader(new InputStreamReader(this._input_, "ISO-8859-1"));
        this._writer = new BufferedWriter(new OutputStreamWriter(this._output_, "ISO-8859-1"));
        HostnameVerifier hostnameVerifier = this.hostnameVerifier;
        if (hostnameVerifier != null && !hostnameVerifier.verify(hostAddress, sSLSocket.getSession())) {
            throw new SSLHandshakeException("Hostname doesn't match certificate");
        }
    }
```

------------------------------------------------
```
#5
Class: org.apache.commons.net.imap.IMAPSClient
Method: void performSSLNegotiation()
Apk Num:10

Apk:io.github.ismywebsiteup_11.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.gianlu.aria2app_221.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:fr.gouv.etalab.mastodon_383.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:li.klass.fhem_141.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:org.courville.nova_404911.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.rfo.basic_500.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.gs.mobileprint_1.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:app.fedilab.lite_383.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:com.rfo.LASKmobile_501.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Apk:org.fdroid.nearby_2.apk
Err: Didn't manually verify hostname in performSSLNegotiation in <org.apache.commons.net.imap.IMAPSClient: void performSSLNegotiation()>::performSSLNegotiation.

Misuse Num:10
```

FP: Forward slicing only take the slicing result of final statement in the graph of a method. However, the taken branch is an additinal null check ` if (hostnameVerifier != null && ... )` and will result in a slicing result without containing `hostnameVerifier.verify(hostAddress, sSLSocket.getSession())`.

Source code snippet:
```
private void performSSLNegotiation() throws IOException {
        initSSLContext();
        SSLSocketFactory socketFactory = this.context.getSocketFactory();
        String hostAddress = this._hostname_ != null ? this._hostname_ : getRemoteAddress().getHostAddress();
        SSLSocket sSLSocket = (SSLSocket) socketFactory.createSocket(this._socket_, hostAddress, getRemotePort(), true);
        sSLSocket.setEnableSessionCreation(true);
        sSLSocket.setUseClientMode(true);
        if (this.tlsEndpointChecking) {
            SSLSocketUtils.enableEndpointNameVerification(sSLSocket);
        }
        String[] strArr = this.protocols;
        if (strArr != null) {
            sSLSocket.setEnabledProtocols(strArr);
        }
        String[] strArr2 = this.suites;
        if (strArr2 != null) {
            sSLSocket.setEnabledCipherSuites(strArr2);
        }
        sSLSocket.startHandshake();
        this._socket_ = sSLSocket;
        this._input_ = sSLSocket.getInputStream();
        this._output_ = sSLSocket.getOutputStream();
        this._reader = new CRLFLineReader(new InputStreamReader(this._input_, "ISO-8859-1"));
        this.__writer = new BufferedWriter(new OutputStreamWriter(this._output_, "ISO-8859-1"));
        HostnameVerifier hostnameVerifier = this.hostnameVerifier;
        if (hostnameVerifier != null && !hostnameVerifier.verify(hostAddress, sSLSocket.getSession())) {
            throw new SSLHandshakeException("Hostname doesn't match certificate");
        }
    }
```

------------------------------------------------
```
#6
Class: cz.msebera.android.httpclient.impl.pool.BasicConnFactory
Method: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)
Apk Num:9

Apk:io.github.ismywebsiteup_11.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:org.twistedappdeveloper.statocovid19italia_35.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:org.mfri.bbcworldservicenewshourdownloader_133.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:org.andstatus.app_349.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:com.rehanced.lunary_31.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:org.thosp.yourlocalweather_144.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:com.yassirh.digitalocean_32.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:es.wolfi.app.passman_13.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Apk:com.danhasting.radar_4.apk
Err: Didn't manually verify hostname in create in <cz.msebera.android.httpclient.impl.pool.BasicConnFactory: cz.msebera.android.httpclient.HttpClientConnection create(cz.msebera.android.httpclient.HttpHost)>::create.

Misuse Num:9
```

TP

------------------------------------------------
```
#7
Class: com.sun.mail.util.SocketFetcher
Method: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)
Apk Num:8

Apk:eu.faircode.email_1818.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:com.oF2pks.jquarks_15.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:org.dystopia.email_116.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:de.grobox.blitzmail_14.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:org.decsync.cc_35.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:se.erikofsweden.findmyphone_13.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:org.kore.kolabnotes.android_105.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Apk:com.Pau.ImapNotes2_40.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.lang.String,java.util.Properties,java.lang.String)>::startTLS.

Misuse Num:8
```

ITP: [use other ways to check hostname in mail context instead of calling `HostnameVerifier.verify()`.] (https://github.com/eclipse-ee4j/angus-mail/blob/6ea88521978dc7870f2a50a6098b7f96ea824f17/core/src/main/java/com/sun/mail/util/SocketFetcher.java#L705)

------------------------------------------------
```
#8
Class: org.eclipse.jetty.util.ssl.SslContextFactory
Method: javax.net.ssl.SSLSocket newSslSocket()
Apk Num:7

Apk:io.github.ismywebsiteup_11.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Apk:com.m3sv.plainupnp_75.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Apk:github.daneren2005.dsub_207.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Apk:org.courville.nova_404911.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Apk:com.matt.outfield_3.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Apk:de.yaacc_26.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Apk:org.droidupnp_18.apk
Err: Didn't manually verify hostname in newSslSocket in <org.eclipse.jetty.util.ssl.SslContextFactory: javax.net.ssl.SSLSocket newSslSocket()>::newSslSocket.

Misuse Num:7
```

ITP: a simple method is only used to `createSocket()`, but later callsites of this method used `SSLParameters.setEndpointIdentificationAlgorithm(HTTPS); SSLSocket.setSSLParameters(SSLParameters);` to ensure hostname verification.
[This is added in API Level 24](https://developer.android.com/reference/javax/net/ssl/SSLParameters#setEndpointIdentificationAlgorithm(java.lang.String)

------------------------------------------------
```
#9
Class: com.sun.mail.util.SocketFetcher
Method: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)
Apk Num:6

Apk:fr.gouv.etalab.mastodon_383.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)>::startTLS.

Apk:com.jadn.cc_173.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)>::startTLS.

Apk:net.vreeken.quickmsg_16.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)>::startTLS.

Apk:es.cesar.quitesleep_13.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)>::startTLS.

Apk:app.fedilab.lite_383.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)>::startTLS.

Apk:net.sourceforge.dibdib.android.dib2qm_2275.apk
Err: Didn't manually verify hostname in startTLS in <com.sun.mail.util.SocketFetcher: java.net.Socket startTLS(java.net.Socket,java.util.Properties,java.lang.String)>::startTLS.

Misuse Num:6
```

TP

------------------------------------------------
```
#10
Class: com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory
Method: void <clinit>()
Apk Num:5

Apk:com.zegoggles.smssync_1576.apk
Err: Didn't manually verify hostname in clinit in <com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory: void <clinit>()>::clinit.

Apk:com.fsck.k9_28006.apk
Err: Didn't manually verify hostname in clinit in <com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory: void <clinit>()>::clinit.

Apk:com.github.axet.smsgate_264.apk
Err: Didn't manually verify hostname in clinit in <com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory: void <clinit>()>::clinit.

Apk:security.pEp_470.apk
Err: Didn't manually verify hostname in clinit in <com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory: void <clinit>()>::clinit.

Apk:one.librem.mail_1010001.apk
Err: Didn't manually verify hostname in clinit in <com.fsck.k9.mail.ssl.DefaultTrustedSocketFactory: void <clinit>()>::clinit.

Misuse Num:5
```

FP: The hostname verification is implemented in `checkServerTrusted` of `TrustManagerFactory`, which generates a `TrustManager` into `sslContext.init(keyManagers, trustManagers, null);`.


------------------------------------------------
```
#11
Class: org.jivesoftware.smack.tcp.XMPPTCPConnection
Method: void proceedTLSReceived()
Apk Num:4

Apk:org.kontalk_500.apk
Err: Didn't manually verify hostname in proceedTLSReceived in <org.jivesoftware.smack.tcp.XMPPTCPConnection: void proceedTLSReceived()>::proceedTLSReceived.

Apk:com.xabber.android_644.apk
Err: Didn't manually verify hostname in proceedTLSReceived in <org.jivesoftware.smack.tcp.XMPPTCPConnection: void proceedTLSReceived()>::proceedTLSReceived.

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Didn't manually verify hostname in proceedTLSReceived in <org.jivesoftware.smack.tcp.XMPPTCPConnection: void proceedTLSReceived()>::proceedTLSReceived.

Apk:org.atalk.android_208010.apk
Err: Didn't manually verify hostname in proceedTLSReceived in <org.jivesoftware.smack.tcp.XMPPTCPConnection: void proceedTLSReceived()>::proceedTLSReceived.

Misuse Num:4
```

FP: Forward slicing only take the slicing result of final statement in the graph of a method. However, the code indeed called the `HostnameVerifier.verify()`.
