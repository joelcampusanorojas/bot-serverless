# Bot Serverless on Azure
This is an example project to deploy a chatbot on Azure working with the next list of services:
  - [Bot Framework](https://dev.botframework.com) Provides tools to build, test, deploy, and manage intelligent bots.
  - [Azure Function Python](https://azure.microsoft.com/en-us/services/functions/) Process and resolve the request and get action in communicate the Bot Framework.
  - [LUIS](https://www.luis.ai) The Natural Language Process (NLP) to understand the message send for the user.
  - [Azure Search](https://azure.microsoft.com/en-us/services/search/) Provides the powerfull to search the mensagges in the Cosmos DB, SQL Server, File Storage.
  - [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) Manage the credential and keys to all project.
  - [Azure Storage](https://azure.microsoft.com/en-us/services/storage/) Storage the file CSV from load the knowledge base

## Motivation
The motivation for this project is the generate the bot with all services with architecture serverless, taking advantage of scale, low cost and easy to deploy and configure.

## Architecture
This is a conversational bot flow that functions search the information in the CVS File.

![Architecture](https://https://github.com/joelcampusanorojas/bot-serverless/images/architecture.png)

  - The user connect to the chatbot for any channel, for example Skype, MS Teams or Slack.
  - The message sent a request to Bot Framework and resolve with Azure Function.
  - The message in the Azure Function call the API in LUIS for understant the intentions.
  - When LUIS indentificate the intentions for the user, in this example greeting, goodbyes or knowledge base.
  - If the intentions was greeting or goodbyes, response a simple static message.
  - If the intentions was knowledge base, search the message in the Azure Search tha was previously load with the CSV file.
