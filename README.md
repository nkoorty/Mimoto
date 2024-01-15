![Mimoto_SCF](https://github.com/nkoorty/Mimoto/assets/80065244/83d3db73-e848-49e5-93b3-7c1621f25fa6)
# Mimoto
Mimoto simplifies digital payments by seamlessly integrating with social media platforms like Discord and Twitter, allowing users to easily send and receive money through user-friendly, personalized links. Built on Stellar, and enhanced with Soroban smart contracts, Mimoto offers a straightforward solution for quick transactions without the complexity of traditional payment methods. This is particularly effective for micro-transactions and social media tipping, providing a hassle-free, secure alternative that's accessible even to those with minimal technical knowledge. With Mimoto, sending money is as simple as sharing a link, improvving the way we think about and execute digital payments in our everyday social interactions.
## Repository Breakdown
### Smart Contracts
Contains all Soroban smart contract code, including the logic for token transactions, user authorization, and other contract-based operations essential to Mimoto's functionality.

### Frontend
Holds the source code for the web-based frontend interface, built with Next.js, providing users with a sleek and responsive platform to manage their digital payments. To run the frontend, run

    npm i
    npm run dev

Аnd find the frontend under `localhost:3000`.

### REST API
The REST API, created with Flask, is the communication layer that connects the frontend to the smart contracts and Firestore database, handling requests and business logic.

### Chromium Extension
Comprises the code for the Chromium-based browser extension, which allows users to interact with Mimoto features directly within their web browsers on social media sites.

### Discord Bot
Includes the implementation of the Mimoto Discord bot, enabling users within Discord servers to easily send and receive payments and view transaction links.
