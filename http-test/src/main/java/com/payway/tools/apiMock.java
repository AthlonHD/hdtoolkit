package com.payway.tools;

import javafx.beans.binding.ObjectExpression;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocketFactory;
import javax.net.ssl.TrustManager;

import java.nio.charset.StandardCharsets;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;

import javax.net.ssl.X509TrustManager;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.SSLSession;


public class apiMock {

    public static class MyX509TrustManager implements X509TrustManager {

        public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
        }

        public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
        }

        public X509Certificate[] getAcceptedIssuers() {
            return null;
        }
    }

    public static class NullHostNameVerifier implements HostnameVerifier{

        public boolean verify(String hostname, SSLSession session) {
            return true;
        }
    }

    public static class httpsRequest {

        public String sendGetRequest(String link, String api) {

            HttpsURLConnection connection = null;
            InputStream is = null;
            BufferedReader br = null;
            String result = null;


            try {
                //设置可通过ip地址访问https请求
                HttpsURLConnection.setDefaultHostnameVerifier(new NullHostNameVerifier());
                TrustManager[] tm = {new MyX509TrustManager()};
                SSLContext sslContext = SSLContext.getInstance("TLS");
                sslContext.init(null, tm, new java.security.SecureRandom());
                // 从上述SSLContext对象中得到SSLSocketFactory对象
                SSLSocketFactory ssf = sslContext.getSocketFactory();

                // 创建远程url连接对象
                URL url = new URL(link + api);
                // 通过远程url连接对象打开一个连接，强转成httpURLConnection类
                connection = (HttpsURLConnection) url.openConnection();

                connection.setSSLSocketFactory(ssf);
                // 设置连接方式：get
                connection.setRequestMethod("GET");
                // 设置请求头
                connection.setRequestProperty("Content-Type", "application/json");
                connection.setRequestProperty("token", "抹去");

                //connection.setRequestProperty("ProfileToken", "F2BCE9044A474C39BF1F8466708C2D9E");
//                connection.setRequestProperty(key, value);
                // 设置连接主机服务器的超时时间：30000毫秒
                connection.setConnectTimeout(30000);
                // 设置读取远程返回的数据时间：
                // connection.setReadTimeout(60000);
                // 发送请求
                connection.connect();
                // 通过connection连接，获取输入流
                if (connection.getResponseCode() == 200) {
                    is = connection.getInputStream();
                    // 封装输入流is，并指定字符集
                    br = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));
                    // 存放数据
                    StringBuilder sbf = new StringBuilder();
                    String temp = null;
                    while ((temp = br.readLine()) != null) {
                        sbf.append(temp);
                        sbf.append("\r\n");
                    }
                    result = sbf.toString();
                    System.out.println(sbf.toString());
//                  return sbf.toString();

                }

            } catch (IOException | NoSuchAlgorithmException | KeyManagementException e) {
                e.printStackTrace();

            } finally {
                // 关闭资源
                if (null != br) {
                    try {
                        br.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }

                if (null != is) {
                    try {
                        is.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }

                // 关闭远程连接
                assert connection != null;
                connection.disconnect();
            }
//            return null;
            return result;
        }
        public String sendGetRequest1(String link, String api,String token) {

            HttpsURLConnection connection = null;
            InputStream is = null;
            BufferedReader br = null;
            String result = null;


            try {
                //设置可通过ip地址访问https请求
                HttpsURLConnection.setDefaultHostnameVerifier(new NullHostNameVerifier());
                TrustManager[] tm = {new MyX509TrustManager()};
                SSLContext sslContext = SSLContext.getInstance("TLS");
                sslContext.init(null, tm, new java.security.SecureRandom());
                // 从上述SSLContext对象中得到SSLSocketFactory对象
                SSLSocketFactory ssf = sslContext.getSocketFactory();

                // 创建远程url连接对象
                URL url = new URL(link + api);
                // 通过远程url连接对象打开一个连接，强转成httpURLConnection类
                connection = (HttpsURLConnection) url.openConnection();

                connection.setSSLSocketFactory(ssf);
                // 设置连接方式：get
                connection.setRequestMethod("GET");
                // 设置请求头
                connection.setRequestProperty("Content-Type", "application/json");
                if(token!=null){
                    connection.setRequestProperty("token", token);
                }else { connection.setRequestProperty("token", "抹去");}

                //connection.setRequestProperty("ProfileToken", "F2BCE9044A474C39BF1F8466708C2D9E");
//                connection.setRequestProperty(key, value);
                // 设置连接主机服务器的超时时间：30000毫秒
                connection.setConnectTimeout(30000);
                // 设置读取远程返回的数据时间：
                // connection.setReadTimeout(60000);
                // 发送请求
                connection.connect();
                // 通过connection连接，获取输入流
                if (connection.getResponseCode() == 200) {
                    is = connection.getInputStream();
                    // 封装输入流is，并指定字符集
                    br = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));
                    // 存放数据
                    StringBuilder sbf = new StringBuilder();
                    String temp = null;
                    while ((temp = br.readLine()) != null) {
                        sbf.append(temp);
                        sbf.append("\r\n");
                    }
                    result = sbf.toString();
                    System.out.println(sbf.toString());
//                  return sbf.toString();

                }

            } catch (IOException | NoSuchAlgorithmException | KeyManagementException e) {
                e.printStackTrace();

            } finally {
                // 关闭资源
                if (null != br) {
                    try {
                        br.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }

                if (null != is) {
                    try {
                        is.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }

                // 关闭远程连接
                assert connection != null;
                connection.disconnect();
            }
//            return null;
            return result;
        }
        public String sendPostRequest(String link, String api,String param,String token) {
            HttpsURLConnection connection = null;
            InputStream is = null;
            OutputStream os = null;
            BufferedReader br = null;
            String result = null;

            try {
                //设置可通过ip地址访问https请求
                HttpsURLConnection.setDefaultHostnameVerifier(new NullHostNameVerifier());
                TrustManager[] tm = {new MyX509TrustManager()};
                SSLContext sslContext = SSLContext.getInstance("TLS");
                sslContext.init(null, tm, new java.security.SecureRandom());
                // 从上述SSLContext对象中得到SSLSocketFactory对象
                SSLSocketFactory ssf = sslContext.getSocketFactory();

                URL url = new URL(link + api);
                // 通过远程url连接对象打开连接
                connection = (HttpsURLConnection) url.openConnection();
                connection.setSSLSocketFactory(ssf);

                // 设置连接请求方式
                connection.setRequestMethod("POST");
                // 设置连接主机服务器超时时间：15000毫秒
                connection.setConnectTimeout(15000);
                // 设置读取主机服务器返回数据超时时间：60000毫秒
//                connection.setReadTimeout(60000);

                // 默认值为：false，当向远程服务器传送数据/写数据时，需要设置为true
                connection.setDoOutput(true);
                // 默认值为：true，当前向远程服务读取数据时，设置为true，该参数可有可无
                connection.setDoInput(true);
                // 设置请求头
                connection.setRequestProperty("Content-Type", "application/json");
                if(token!=null){
                    connection.setRequestProperty("token",token);
                }
                else {
                    connection.setRequestProperty("token", "抹去");
                }
                  //       connection.setRequestProperty(key, value);
                // 通过连接对象获取一个输出流 😉
                os = connection.getOutputStream();
                // 通过输出流对象将参数写出去/传输出去,它是通过字节数组写出的
                os.write(param.getBytes());
                // 通过连接对象获取一个输入流，向远程读取
                if (connection.getResponseCode() == 200) {

                    is = connection.getInputStream();
                    // 对输入流对象进行包装:charset根据工作项目组的要求来设置
                    br = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));

                    StringBuilder sbf = new StringBuilder();
                    String temp = null;
                    // 循环遍历一行一行读取数据
                    while ((temp = br.readLine()) != null) {
                        sbf.append(temp);
                        sbf.append("\r\n");
                    }
                    result = sbf.toString();
                    System.out.println(result);
                }
            } catch (IOException | NoSuchAlgorithmException | KeyManagementException e) {
                e.printStackTrace();

            } finally {
                // 关闭资源
                if (null != br) {
                    try {
                        br.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                if (null != os) {
                    try {
                        os.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                if (null != is) {
                    try {
                        is.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                // 断开与远程地址url的连接
                assert connection != null;
                connection.disconnect();
            }
            return result;
        }


    }


}