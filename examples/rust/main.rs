use reqwest::Client;
use serde::{Deserialize};
use std::error::Error;

const CLIENT_ID: &str = "your_client_id";
const CLIENT_SECRET: &str = "your_client_secret";
const REDIRECT_URI: &str = "your_redirect_uri";
const AUTH_CODE: &str = "your_authorization_code";

#[derive(Debug, Deserialize)]
struct TokenResponse {
    access_token: String,
    token_type: String,
    expires_in: u64,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let token = get_access_token().await?;
    get_organization(&token).await?;
    Ok(())
}

async fn get_access_token() -> Result<String, Box<dyn Error>> {
    let client = Client::new();

    let params = [
        ("grant_type", "authorization_code"),
        ("code", AUTH_CODE),
        ("client_id", CLIENT_ID),
        ("client_secret", CLIENT_SECRET),
        ("redirect_uri", REDIRECT_URI),
    ];

    let res = client.post("https://api.3plguys.com/oauth/token")
        .form(&params)
        .send()
        .await?;

    if !res.status().is_success() {
        let err = res.text().await?;
        return Err(format!("❌ Token error: {}", err).into());
    }

    let token: TokenResponse = res.json().await?;
    println!("✅ Access token: {}", token.access_token);
    Ok(token.access_token)
}

async fn get_organization(token: &str) -> Result<(), Box<dyn Error>> {
    let client = Client::new();

    let res = client.get("https://api.3plguys.com/v0/organization")
        .bearer_auth(token)
        .send()
        .await?;

    if !res.status().is_success() {
        let err = res.text().await?;
        return Err(format!("❌ Org error: {}", err).into());
    }

    let org = res.text().await?;
    println!("🏢 Organization:\n{}", org);
    Ok(())
}
