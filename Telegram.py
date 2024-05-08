# import telegram.ext


# Token="6996215541:AAGr52FY7Nh9JCce0Bmas4sxxu_bBYktw5E"

# updater=telegram.ext.Updater("6996215541:AAGr52FY7Nh9JCce0Bmas4sxxu_bBYktw5E",update_queue=True)
# dispatch=updater.dispatcher

# def start(update,context):
#     update.message.reply_text("Hello welcome to Vivin Chat bot")
    
# dispatcher.add_handler(telegram.ext.CommandHandler('start',start))


# updater.start_polling()
# updater.idle()


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6996215541:AAGr52FY7Nh9JCce0Bmas4sxxu_bBYktw5E'
BOT_USERNAME = 'nanichatbot'

# Define command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "I am a Python bot. Here are the commands you can use:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/context - Show a brief description of the chatbot\n"
        "/topoffers - Get the top offers\n"
        "/mobiles - Explore mobiles and tablets\n"
        "/tvappliances - Discover TVs and appliances\n"
        "/electronics - View electronics deals\n"
        "/fashion - Check out fashion deals\n"
        "/beauty - Explore beauty products\n"
        "/homekitchen - Discover home and kitchen products\n"
        "/grocery - Explore grocery items\n"
        "/question1 - Q: How can I find the best deals on Flipkart?\n"
        "/question2 - Q: How often are the deals updated on Flipkart?\n"
        "/question3 - Q: Are there any special discounts for specific payment methods?\n"
    )
    await update.message.reply_text(help_text)

async def context_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context_text = (
        "Welcome to Nani Chat Bot!\n\n"
        "I'm here to provide you with the latest Flipkart deals and offers.\n"
        "You can use various commands to explore different categories of deals."
        
    )
    await update.message.reply_text(context_text)



async def topoffers_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Check out the top offers here: [Top Offers](https://www.flipkart.com/offers-store?fm=neo%2Fmerchandising&iid=M_62ddf9d1-2cfc-46dd-98ef-f72eb1402204_1_KUZ8W60OFFMO_MC.PLA0IVF1DX7W&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Top%2BOffer_PLA0IVF1DX7W&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L0_view-all&cid=PLA0IVF1DX7W)")

async def mobiles_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Explore mobiles and tablets here: [Mobiles and Tablets](https://www.flipkart.com/mobile-phones-big-saving-days-may-24-1ax-store?fm=neo%2Fmerchandising&iid=M_eae86561-cefc-41f2-9516-a8a6ebd5b7f1_1_KUZ8W60OFFMO_MC.BYIXDBQAWBHQ&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles%2B%2526%2BTablets_BYIXDBQAWBHQ&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=BYIXDBQAWBHQ)")

async def tvappliances_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Discover TVs and appliances here: [TVs and Appliances](https://www.flipkart.com/tv-and-appliances-big-savings-days-sale-store?fm=neo%2Fmerchandising&iid=M_8b22535c-f6e9-4747-8d0a-aa200157f438_1_KUZ8W60OFFMO_MC.8TVKUWT87M16&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_TVs%2B%2526%2BAppliances_8TVKUWT87M16&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L0_view-all&cid=8TVKUWT87M16)")

async def electronics_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("View electronics deals here: [Electronics](https://www.flipkart.com/elec-big-saving-days-may-24-sale-store?fm=neo%2Fmerchandising&iid=M_9918a119-f899-4ad3-aa98-967edd110684_1_KUZ8W60OFFMO_MC.KCBBC8GGWR9V&otracker=hp_rich_navigation_4_1.navigationCard.RICH_NAVIGATION_Electronics_KCBBC8GGWR9V&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L0_view-all&cid=KCBBC8GGWR9V)")

async def fashion_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Check out fashion deals here: [Fashion](https://www.flipkart.com/bsd-may-base24-store?fm=neo%2Fmerchandising&iid=M_b77fd2cd-6402-4e08-b20a-24071f66e1f3_1_KUZ8W60OFFMO_MC.NT4YVV713W2Q&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Fashion_NT4YVV713W2Q&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L0_view-all&cid=NT4YVV713W2Q)")

async def beauty_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Explore beauty products here: [Beauty](https://www.flipkart.com/big-saving-days-sale-j24-store?fm=neo%2Fmerchandising&iid=M_96d633e5-4ac0-4efb-a025-d1180d141dd1_1_KUZ8W60OFFMO_MC.3HG9V6MXYB5P&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Beauty_3HG9V6MXYB5P&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L0_view-all&cid=3HG9V6MXYB5P)")

async def homekitchen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Discover home and kitchen products here: [Home and Kitchen](https://www.flipkart.com/hnf-bsd-store?fm=neo%2Fmerchandising&iid=M_167170f8-a994-4097-8f4e-231e1569db27_1_KUZ8W60OFFMO_MC.IF1WVE47NIXO&otracker=hp_rich_navigation_7_1.navigationCard.RICH_NAVIGATION_Home%2B%2526%2BKitchen_IF1WVE47NIXO&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L0_view-all&cid=IF1WVE47NIXO)")

async def grocery_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Explore grocery items here: [Grocery](https://www.flipkart.com/grocery-supermart-store?marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_4cffb5c2-071f-4461-9c7b-ce7e82df26e6_1_KUZ8W60OFFMO_MC.4BYE6NISISOE&otracker=hp_rich_navigation_10_1.navigationCard.RICH_NAVIGATION_Grocery_4BYE6NISISOE&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_10_L0_view-all&cid=4BYE6NISISOE)")

# Define message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Your message handling logic goes here
    pass

# Define error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
# Define question1 command handler
async def question1_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = (
        "Q: How can I find the best deals on Flipkart?\n\n"
        "A: To find the best deals on Flipkart, you can visit the 'Top Offers' section by using the /topoffers command. "
        "This section showcases the latest and most popular deals across various categories including electronics, fashion, home & kitchen, and more. "
        "Additionally, you can explore specific categories such as mobiles, TVs & appliances, fashion, beauty, etc., by using their respective commands. "
        "These commands will provide you with direct links to the corresponding deal pages where you can browse and shop for your favorite products."
    )
    await update.message.reply_text(response)

# Define question2 command handler
async def question2_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = (
        "Q: How often are the deals updated on Flipkart?\n\n"
        "A: Flipkart regularly updates its deals and offers to provide customers with fresh discounts and promotions. "
        "While some deals may last for a limited time, new deals are frequently added across various categories. "
        "To stay updated with the latest offers, you can check the Flipkart website or use this chatbot to explore the latest deals using the available commands."
    )
    await update.message.reply_text(response)

# Define question3 command handler
async def question3_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = (
        "Q: Are there any special discounts for specific payment methods?\n\n"
        "A: Yes, Flipkart often offers special discounts and cashback offers for specific payment methods such as credit/debit cards, "
        "UPI payments, and wallet payments. These offers may vary depending on ongoing promotions and partnerships with payment providers. "
        "To take advantage of these discounts, be sure to check the payment options available during checkout and look out for any applicable offers."
    )
    await update.message.reply_text(response)

if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('context', context_command))
    app.add_handler(CommandHandler('topoffers', topoffers_command))
    app.add_handler(CommandHandler('mobiles', mobiles_command))
    app.add_handler(CommandHandler('tvappliances', tvappliances_command))
    app.add_handler(CommandHandler('electronics', electronics_command))
    app.add_handler(CommandHandler('fashion', fashion_command))
    app.add_handler(CommandHandler('beauty', beauty_command))
    app.add_handler(CommandHandler('homekitchen', homekitchen_command))
    app.add_handler(CommandHandler('grocery', grocery_command))
    app.add_handler(CommandHandler('question1', question1_command))
    app.add_handler(CommandHandler('question2', question2_command))
    app.add_handler(CommandHandler('question3', question3_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Register error handler
    app.add_error_handler(error)

    # Start polling
    print("Polling...")
    app.run_polling(poll_interval=3)
