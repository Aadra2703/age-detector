module MyCoin::Coin {

    use std::signer;
    use aptos_framework::coin::{Self, CoinStore, mint, transfer};
    use aptos_framework::account;
    
    struct MyCoin has store {
        value: u64,
    }

    /// Initialize the coin information, similar to before.
    public entry fun initialize(creator: &signer) {
        let coin_name = b"MyCoin";
        let coin_symbol = b"MC";
        let decimals = 6;
        aptos_framework::coin::initialize<MyCoin>(
            creator, 
            coin_name, 
            coin_symbol, 
            decimals
        );
    }

    /// Mint coins based on age and gender
    public entry fun mint_based_on_age_gender(
        creator: &signer, 
        recipient: address, 
        age: u8, 
        gender: u8, 
        base_amount: u64
    ) {
        let final_amount = calculate_amount_based_on_age_gender(age, gender, base_amount);
        mint<MyCoin>(creator, recipient, final_amount);
    }

    /// Calculate minting amount based on age and gender
    fun calculate_amount_based_on_age_gender(age: u8, gender: u8, base_amount: u64): u64 {
        // Example logic:
        //  - If age > 18 and gender == 1 (assuming 1 is male), mint more coins
        //  - If age <= 18 and gender == 0 (female), mint fewer coins

        if (age > 18 && gender == 1) {
            // Increase amount for adults (males)
            base_amount * 2
        } else if (age <= 18 && gender == 0) {
            // Decrease amount for minors (females)
            base_amount / 2
        } else {
            base_amount
        }
    }

    /// Transfer coins, same as before
    public entry fun transfer(sender: &signer, recipient: address, amount: u64) {
        transfer<MyCoin>(sender, recipient, amount);
    }

    /// Check balance, same as before
    public fun balance_of(account: &address): u64 {
        let store = aptos_framework::coin::balance<MyCoin>(account);
        store.value
    }
}
