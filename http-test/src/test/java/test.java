import java.io.UnsupportedEncodingException;

public class test {
    public static void main(String[] args) throws UnsupportedEncodingException {
        apiMock.httpsRequest r = new apiMock.httpsRequest();

        String json = "{\"MediaType\": \"WeChat\", " +
                "\"SocialCode\": \"GH1NB1EDD14HJK5NFG\", " +
                "\"AddTime\": \"2021-02-21\"}";
        r.sendPostRequest("/api/Profile/BindSocial", "ProfileToken", "F2BCE9044A474C39BF1F8466708C2D" +
                "9E", json);

        r.sendGetRequest("/api/Profile/GetSocial?MediaCode=WeChat", "ProfileToken", "F2BCE9044A474C39" +
                "BF1F8466708C2D9E");
    }
}