import requests
import time
import random
from datetime import datetime, timedelta
import os
import sys

def refresh_nft_metadata(contract_address, token_id, api_key):
    refresh_url = f"https://api.opensea.io/api/v2/chain/ethereum/contract/{contract_address}/nfts/{token_id}/refresh"
    
    headers = {
        "Accept": "application/json",
        "X-API-KEY": api_key
    }
    
    try:
        response = requests.post(refresh_url, headers=headers, timeout=30)
        if response.status_code == 200:
            print(f"Successfully queued refresh for NFT with token ID: {token_id}")
            return True
        else:
            print(f"Failed to queue refresh for NFT with token ID: {token_id}. Status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Error refreshing NFT with token ID {token_id}: {e}")
        return False

def should_run_today(target_dates):
    today = datetime.utcnow().date()  # Using UTC date
    return today in target_dates

def main():
    contract_address = "0x95ab7a1f8cf303a9724e077b34483372907e0701"  # For "The White Room"
    api_key = os.getenv("OPENSEA_API_KEY")  # Get from environment (set in GitHub secrets)
    if not api_key:
        print("Error: OPENSEA_API_KEY not set.")
        sys.exit(1)

    # Parse token range from command-line args (default: 1 to 4800)
    if len(sys.argv) == 3:
        min_token = int(sys.argv[1])
        max_token = int(sys.argv[2])
    else:
        min_token = 1
        max_token = 4800

    # List of target dates in UTC (fixed typos, e.g., 2024 -> 2025)
    target_dates = [
        datetime(2025, 1, 3).date(),         # Birth of BTC
        datetime(2025, 1, 5, 0, 1).date(),   # Return to normal for BTC
        datetime(2025, 1, 28).date(),        # NASA Day
        datetime(2025, 1, 30, 0, 1).date(),  # Return to normal for NASA Day
        datetime(2025, 2, 9).date(),         # Pizza Day
        datetime(2025, 2, 11, 0, 1).date(),  # Return to normal for Pizza Day
        datetime(2025, 3, 2).date(),         # Dr. Seuss Day
        datetime(2025, 3, 4, 0, 1).date(),   # Return to normal for Dr. Seuss Day
        datetime(2025, 3, 14).date(),        # Pi Day
        datetime(2025, 3, 16, 0, 1).date(),  # Return to normal for Pi Day
        datetime(2025, 3, 31).date(),        # Matrix Day
        datetime(2025, 4, 10, 0, 1).date(),  # Return to normal for Matrix Day
        datetime(2025, 4, 20).date(),        # 420
        datetime(2025, 4, 22, 0, 1).date(),  # Return to normal for 420
        datetime(2025, 5, 3).date(),         # Wu Tang day
        datetime(2025, 5, 5, 0, 1).date(),   # Return to normal for Wu Tang day
        datetime(2025, 5, 4).date(),         # May the fourth be with you (Star Wars)
        datetime(2025, 5, 6, 0, 1).date(),   # Return to normal for Star Wars Day
        datetime(2025, 5, 7).date(),         # Beer pong day
        datetime(2025, 5, 9, 0, 1).date(),   # Return to normal for Beer pong day
        datetime(2025, 5, 11).date(),        # Christie Punk auction (9 CPs for 17Mil)
        datetime(2025, 5, 13, 0, 1).date(),  # Return to normal for Christie Punk auction
        datetime(2025, 5, 22).date(),        # Bitcoin Pizza day
        datetime(2025, 5, 24, 0, 1).date(),  # Return to normal for Bitcoin Pizza day
        datetime(2025, 6, 3).date(),         # Egg Day
        datetime(2025, 6, 5, 0, 1).date(),   # Return to normal for Egg Day
        datetime(2025, 6, 5).date(),         # Environment Day
        datetime(2025, 6, 7, 0, 1).date(),   # Return to normal for Environment Day
        datetime(2025, 6, 9).date(),         # Sex day
        datetime(2025, 6, 11, 0, 1).date(),  # Return to normal for Sex day
        datetime(2025, 6, 23).date(),        # Birth of Crypto punks
        datetime(2025, 6, 25, 0, 1).date(),  # Return to normal for Crypto punks
        datetime(2025, 7, 2).date(),         # UFO Day
        datetime(2025, 7, 4, 0, 1).date(),   # Return to normal for UFO Day
        datetime(2025, 7, 30).date(),        # Birth of ETH
        datetime(2025, 8, 1, 0, 1).date(),   # Return to normal for Birth of ETH
        datetime(2025, 8, 17).date(),        # Thrift store day
        datetime(2025, 8, 19, 0, 1).date(),  # Return to normal for Thrift store day
        datetime(2025, 8, 23).date(),        # Visa buys punk
        datetime(2025, 8, 25, 0, 1).date(),  # Return to normal for Visa buys punk
        datetime(2025, 8, 30).date(),        # Toasted Marshmallow day
        datetime(2025, 9, 1, 0, 1).date(),   # Return to normal for Toasted Marshmallow day
        datetime(2025, 9, 7).date(),         # El Salvador adopts BTC
        datetime(2025, 9, 9, 0, 1).date(),   # Return to normal for El Salvador adopts BTC
        datetime(2025, 9, 12).date(),        # Video game day
        datetime(2025, 9, 14, 0, 1).date(),  # Return to normal for Video game day
        datetime(2025, 9, 29).date(),        # Bubble gum day
        datetime(2025, 10, 1, 0, 1).date(),  # Return to normal for Bubble gum day
        datetime(2025, 10, 1).date(),        # Apprehension of Ross Ulbricht
        datetime(2025, 10, 3, 0, 1).date(),  # Return to normal for Ross Ulbricht
        datetime(2025, 10, 5).date(),        # Banksy shreds art making art
        datetime(2025, 10, 7, 0, 1).date(),  # Return to normal for Banksy art
        datetime(2025, 10, 6).date(),        # Birth of morphing Museum Punks
        datetime(2025, 10, 8, 0, 1).date(),  # Return to normal for Museum Punks
        datetime(2025, 10, 9).date(),        # Fire prevention day
        datetime(2025, 10, 11, 0, 1).date(), # Return to normal for Fire prevention day
        datetime(2025, 10, 13).date(),       # No bra day
        datetime(2025, 10, 15, 0, 1).date(), # Return to normal for No bra day
        datetime(2025, 10, 16).date(),       # World food day
        datetime(2025, 10, 18, 0, 1).date(), # Return to normal for World food day
        datetime(2025, 10, 22).date(),       # Color day feat. Campbell La Pun
        datetime(2025, 10, 24, 0, 1).date(), # Return to normal for Color day
        datetime(2025, 10, 25).date(),       # Picasso's birthday
        datetime(2025, 10, 27, 0, 1).date(), # Return to normal for Picasso's birthday
        datetime(2025, 10, 31).date(),       # Halloween
        datetime(2025, 11, 2, 0, 1).date(),  # Return to normal for Halloween
        datetime(2025, 11, 3).date(),        # Stress awareness day
        datetime(2025, 11, 5, 0, 1).date(),  # Return to normal for Stress awareness day
        datetime(2025, 11, 5).date(),        # Guy Fawkes Night day
        datetime(2025, 11, 7, 0, 1).date(),  # Return to normal for Guy Fawkes Night
        datetime(2025, 11, 9).date(),        # Berlin Wall falls 1989
        datetime(2025, 11, 11, 0, 1).date(), # Return to normal for Berlin Wall
        datetime(2025, 11, 16).date(),       # Fast food day feat. Fast Food Punks
        datetime(2025, 11, 18, 0, 1).date(), # Return to normal for Fast food day
        datetime(2025, 11, 18).date(),       # Birth of Mickey Mouse
        datetime(2025, 11, 20, 0, 1).date(), # Return to normal for Mickey Mouse
        datetime(2025, 11, 21).date(),       # Television day
        datetime(2025, 11, 23, 0, 1).date(), # Return to normal for Television day
        datetime(2025, 11, 25).date(),       # Thanksgiving
        datetime(2025, 11, 27, 0, 1).date(), # Return to normal for Thanksgiving
        datetime(2025, 12, 4).date(),        # Taped banana on the wall sell as art
        datetime(2025, 12, 6, 0, 1).date(),  # Return to normal for Taped banana
        datetime(2025, 12, 10).date(),       # Nobel peace prize day
        datetime(2025, 12, 12, 0, 1).date(), # Return to normal for Nobel peace prize
        datetime(2025, 12, 18).date(),       # Hold day
        datetime(2025, 12, 20, 0, 1).date(), # Return to normal for Hold day (fixed from 2024)
        datetime(2025, 12, 25).date(),       # Christmas
        datetime(2025, 12, 27, 0, 1).date(), # Return to normal for Christmas (fixed from 2024)
        datetime(2025, 1, 1).date(),         # New Year's
        datetime(2025, 1, 3, 0, 1).date(),   # Return to normal for New Year's
    ]

    if should_run_today(target_dates):
        print(f"Starting refresh cycle on {datetime.utcnow().strftime('%Y-%m-%d')} UTC for tokens {min_token} to {max_token}")
        
        # Get all tokens in range, shuffle for random order
        tokens_to_refresh = list(range(min_token, max_token + 1))
        random.shuffle(tokens_to_refresh)
        
        for token_id in tokens_to_refresh:
            if refresh_nft_metadata(contract_address, str(token_id), api_key):
                print(f"Token {token_id} refresh was successful.")
            else:
                print(f"Token {token_id} refresh failed.")
            
            # Random delay between 2 to 8 seconds to avoid rate limits
            delay = random.randint(2, 8)
            print(f"Waiting for {delay} seconds before next refresh.")
            time.sleep(delay)
        
        print(f"Finished refreshing tokens {min_token} to {max_token}.")
    else:
        print(f"Not a target date: {datetime.utcnow().strftime('%Y-%m-%d')} UTC. Exiting.")

if __name__ == "__main__":
    main()
