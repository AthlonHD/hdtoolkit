package com.payway.tools;


import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;


public class UrlEncode {

    public String utf8Encode(String name) throws UnsupportedEncodingException {

        return URLEncoder.encode(name, "utf-8");

    }

}
