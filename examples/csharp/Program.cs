using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    const string ClientId = "your_client_id";
    const string ClientSecret = "your_client_secret";
    const string RedirectUri = "your_redirect_uri";
    const string AuthCode = "your_authorization_code";

    static readonly HttpClient client = new();

    static async Task Main()
    {
        var token = await GetAccessToken();
        if (token != null)
        {
            await GetOrganization(token);
        }
    }

    static async Task<string?> GetAccessToken()
    {
        var body = new StringContent(
            $"grant_type=authorization_code&code={AuthCode}&client_id={ClientId}&client_secret={ClientSecret}&redirect_uri={RedirectUri}",
            Encoding.UTF8,
            "application/x-www-form-urlencoded"
        );

        var res = await client.PostAsync("https://api.3plguys.com/oauth/token", body);

        if (!res.IsSuccessStatusCode)
        {
            Console.WriteLine($"❌ Token error: {res.StatusCode} - {await res.Content.ReadAsStringAsync()}");
            return null;
        }

        using var content = await res.Content.ReadAsStreamAsync();
        var json = await JsonDocument.ParseAsync(content);
        var token = json.RootElement.GetProperty("access_token").GetString();
        Console.WriteLine("✅ Access token retrieved");
        return token;
    }

    static async Task GetOrganization(string token)
    {
        var request = new HttpRequestMessage(HttpMethod.Get, "https://api.3plguys.com/v0/organization");
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var res = await client.SendAsync(request);

        if (!res.IsSuccessStatusCode)
        {
            Console.WriteLine($"❌ Org error: {res.StatusCode} - {await res.Content.ReadAsStringAsync()}");
            return;
        }

        var json = await res.Content.ReadAsStringAsync();
        Console.WriteLine("🏢 Organization info:");
        Console.WriteLine(json);
    }
}
