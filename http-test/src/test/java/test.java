import com.payway.tools.apiMock;

import java.io.UnsupportedEncodingException;

public class test {
    public static void main(String[] args) throws UnsupportedEncodingException {
        apiMock.httpsRequest r = new apiMock.httpsRequest();

        String json = "{\"memberNo\": \"860000000124136\",   \"mediaType\": \"wechat\",   \"socialCode\": \"GH1NB1EDD14HJK5NFG\",   \"social_FirstName\": \"1\",   \"social_LastName\": \"1\",   \"socialBirthDay\": \"2020-10-27\",   \"social_Gender\": 1,   \"social_Email\": \"1\",   \"social_Logo\": \"1\",   \"addTime\": \"2020-09-01\",   \"externalPropertits\": \"1\",   \"methodCode\": \"FB836B3137\",   \"more\": \"more\" }";

        r.sendGetRequest("/api/Profile20/GetMemberDetail?memberNo=860000000116260");

        r.sendPostRequest("/api/Profile20/BindSocial", json);

    }
}