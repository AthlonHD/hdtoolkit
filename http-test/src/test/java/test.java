import com.payway.tools.UrlEncode;

import java.io.UnsupportedEncodingException;

public class test {
    public static void main(String[] args) throws UnsupportedEncodingException {

        String name = "免费领代金券-测试专用领取无效0714150133";

        UrlEncode c = new UrlEncode();

        String rusult = c.utf8Encode(name);

        System.out.println(rusult);
    }
}