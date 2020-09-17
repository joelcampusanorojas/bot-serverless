using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Bot.Builder;
using Microsoft.Bot.Schema;
using System.Net;
using System;
using System.Net.Http;
using System.Text;  // for class Encoding
using System.IO;  
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;

namespace Microsoft.BotBuilderSamples.Bots
{
    public class EchoBot : ActivityHandler
    {
        public class FlaskRequestModel
        {
            [JsonProperty("text")]
            public string Text {get; set;}            
            
        }
    
        protected override async Task OnMessageActivityAsync(ITurnContext<IMessageActivity> turnContext, CancellationToken cancellationToken)
        {           
            var replyText = $"{turnContext.Activity.Text}";
            //if (!replyText.ToLower().Contains("Hey Bot")){  # Optional bit of code that only sends the sends the message to the back end if it contains a particular keyword
            //    return;
            //}
            var replyTextModel = new FlaskRequestModel()
            {
                Text = replyText 
            };

            var jsonObject = JsonConvert.SerializeObject(replyTextModel);
        
            var request = new HttpRequestMessage()
            {

                Content = new StringContent(jsonObject, Encoding.UTF8, "application/json"),
                Method = HttpMethod.Post,
                RequestUri = new Uri("https://bot-serverless-function.azurewebsites.net/api/HttpTrigger"),   //  <- Replace the URL with the the URL for your function app
            };            
        
            var httpClient = new HttpClient();
            // httpClient.DefaultRequestHeaders.Add("API-Key","your API-key");  <- required if your HTTP trigger authorization was set to something other than Anonymous
            var response = await httpClient.SendAsync(request, HttpCompletionOption.ResponseContentRead);      
        
            if (response.IsSuccessStatusCode)
            {
                var responseString = await response.Content.ReadAsStringAsync();
                await turnContext.SendActivityAsync(MessageFactory.Text(responseString, responseString), cancellationToken);
            }
            else
            {
                await turnContext.SendActivityAsync(MessageFactory.Text("failure", "failure"), cancellationToken);
                var responseString = await response.Content.ReadAsStringAsync();
                await turnContext.SendActivityAsync(MessageFactory.Text(responseString, responseString), cancellationToken);   
            }
        }

        protected override async Task OnMembersAddedAsync(IList<ChannelAccount> membersAdded, ITurnContext<IConversationUpdateActivity> turnContext, CancellationToken cancellationToken)
        {
            var welcomeText = "Hello and welcome!";
            foreach (var member in membersAdded)
            {
                if (member.Id != turnContext.Activity.Recipient.Id)
                {
                    await turnContext.SendActivityAsync(MessageFactory.Text(welcomeText, welcomeText), cancellationToken);
                }
            }
        }
    }
}