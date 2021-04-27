import com.payway.tools.apiMock;

import java.io.UnsupportedEncodingException;

import org.json.JSONObject;

public class test {
    public static void main(String[] args) throws UnsupportedEncodingException {
        apiMock.httpsRequest r = new apiMock.httpsRequest();

        String token = r.sendGetRequest("https://uatminiappapi.capitastar.com.cn","/api/MyCenter/GetTokenByPhone?Mobile=15601900263");

//        System.out.println(tokens);

//        String json = "{\"memberNo\":\"860000000124007\",\"pointAmount\":109,\"fromCode\":\"T243567446\",\"fromName\":\"test\",\"description\":\"111111111\",\"validTime\":\"2021-12-0706:18:14.722\",\"mallCode\":\"CN064\",\"ticketNo\":\"257256575683454313123\",\"methodCode\":\"FB836B3137\",\"rollTime\":\"${__timeShift(yyyy-MM-ddHH:mm:ss,,PT1H,,)}\"}";
//        String response = r.sendPostRequest("https://crmmemberuat.dc.capitaland.com", "/api/Point20/HoldPoint_Redemption", json);
//
//        JSONObject response_object = new JSONObject(response);
//        JSONObject response_body = (JSONObject) response_object.get("body");
//        String identifier = (String) response_body.get("identifier");
//        System.out.println(identifier);

    }
}