package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
)

// Replace with real values
const (
	clientID     = "your_client_id"
	clientSecret = "your_client_secret"
	redirectURI  = "your_redirect_uri"
	authCode     = "your_authorization_code"
)

type TokenResponse struct {
	AccessToken string `json:"access_token"`
	TokenType   string `json:"token_type"`
	ExpiresIn   int    `json:"expires_in"`
}

func getAccessToken() (string, error) {
	form := url.Values{}
	form.Set("grant_type", "authorization_code")
	form.Set("code", authCode)
	form.Set("client_id", clientID)
	form.Set("client_secret", clientSecret)
	form.Set("redirect_uri", redirectURI)

	req, err := http.NewRequest("POST", "https://api.3plguys.com/oauth/token", bytes.NewBufferString(form.Encode()))
	if err != nil {
		return "", err
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer res.Body.Close()

	if res.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(res.Body)
		return "", fmt.Errorf("token error %d: %s", res.StatusCode, string(body))
	}

	var tokenResp TokenResponse
	if err := json.NewDecoder(res.Body).Decode(&tokenResp); err != nil {
		return "", err
	}
	fmt.Println("✅ Access token retrieved")
	return tokenResp.AccessToken, nil
}

func getOrganization(token string) error {
	req, err := http.NewRequest("GET", "https://api.3plguys.com/v0/organization", nil)
	if err != nil {
		return err
	}
	req.Header.Set("Authorization", "Bearer "+token)

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}
	defer res.Body.Close()

	if res.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(res.Body)
		return fmt.Errorf("org error %d: %s", res.StatusCode, string(body))
	}

	var org map[string]interface{}
	if err := json.NewDecoder(res.Body).Decode(&org); err != nil {
		return err
	}

	fmt.Printf("🏢 %s\n", org["name"])
	fmt.Printf("Website: %s\n", org["website"])
	contact := org["contact"].(map[string]interface{})
	fmt.Printf("Contact: %s | %s\n", contact["name"], contact["phoneNumber"])
	address := org["address"].(map[string]interface{})
	fmt.Printf("Address: %s, %s, %s %s\n", address["addressline1"], address["city"], address["state"], address["zipcode"])

	return nil
}

func main() {
	token, err := getAccessToken()
	if err != nil {
		fmt.Println("❌", err)
		return
	}

	if err := getOrganization(token); err != nil {
		fmt.Println("❌", err)
	}
}
