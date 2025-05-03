import okhttp3.*;

import java.io.IOException;
import java.util.Objects;

public class Main {
    private static final String CLIENT_ID = "your_client_id";
    private static final String CLIENT_SECRET = "your_client_secret";
    private static final String REDIRECT_URI = "your_redirect_uri";
    private static final String AUTH_CODE = "your_authorization_code";

    private static final OkHttpClient client = new OkHttpClient();

    public static void main(String[] args) throws IOException {
        String token = getAccessToken();
        if (token != null) {
            getOrganization(token);
        }
    }

    private static String getAccessToken() throws IOException {
        RequestBody body = new FormBody.Builder()
                .add("grant_type", "authorization_code")
                .add("code", AUTH_CODE)
                .add("client_id", CLIENT_ID)
                .add("client_secret", CLIENT_SECRET)
                .add("redirect_uri", REDIRECT_URI)
                .build();

        Request request = new Request.Builder()
                .url("https://api.3plguys.com/oauth/token")
                .post(body)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("❌ Token error: " + response.code() + " - " + response.body().string());
                return null;
            }

            String json = Objects.requireNonNull(response.body()).string();
            String accessToken = json.split("\"access_token\":\"")[1].split("\"")[0];
            System.out.println("✅ Access token retrieved");
            return accessToken;
        }
    }

    private static void getOrganization(String token) throws IOException {
        Request request = new Request.Builder()
                .url("https://api.3plguys.com/v0/organization")
                .addHeader("Authorization", "Bearer " + token)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("❌ Org error: " + response.code() + " - " + response.body().string());
                return;
            }

            String json = Objects.requireNonNull(response.body()).string();
            System.out.println("🏢 Organization Info:\n" + json);
        }
    }
}
