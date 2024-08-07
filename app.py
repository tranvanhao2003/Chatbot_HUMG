import gradio as gr
from configs.load_config import LoadConfig
from source.chat import chat_with_history
APP_CFG = LoadConfig()

def reset_conversation():
    # Thêm tin nhắn chào hỏi vào đây
    return [("", "Xin chào! 😊 Em là Bot HUMG, trợ lý tư vấn tuyển sinh tại Đại học Mỏ - Địa chất sẵn sàng tư vấn cho anh/chị về các ngành học tại trường. Rất vui được hỗ trợ anh/chị hôm nay! Chúc anh/chị một ngày tuyệt vời! 😊")], []

with gr.Blocks(css="""
    #chatbot { 
        height: 100%; 
        overflow-y: auto; 
        border: 1px solid #ddd; 
        border-radius: 15px; 
        padding: 20px;
        background-color: #f7f7f7;
    }
    #chatbot .user, #chatbot .bot { 
        padding: 10px 15px; 
        border-radius: 20px; 
        display: inline-block;
    }
    #chatbot .user { 
        background-color: #FF1493; 
        color: black;
        float: right;
    }
    #chatbot .bot { 
        background-color: #F0F8FF; 
        color: black;
        float: left;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    #chat-header {
        text-align: center;
        padding: 20px;
        background-color: #FF1493;
        color: white;
        border-radius: 15px 15px 0 0;
        margin-bottom: 20px;
    }
    #msg-box {
        border-radius: 20px;
        border: 1px solid #ddd;
    }
    #send-btn, #reset-btn, #clear-btn {
        border-radius: 20px;
    }
    .button-row {
        display: flex;
        justify-content: space-between;
        margin-top: 10px;
    }
""") as demo:
    gr.HTML("""
    <div id="chat-header">
        <h1 style="color: #000000">💬 Chatbot tư vấn tuyển sinh Trường đại học Mỏ-Địa chất</h1>
        <p style="color: #000000">Hãy đặt câu hỏi, tôi sẽ cố gắng trả lời bạn!</p>
    </div>
    """)
    
    chatbot = gr.Chatbot(
        [("", "Xin chào! 😊 Em là Bot HUMG, trợ lý tư vấn tuyển sinh tại Đại học Mỏ - Địa chất sẵn sàng tư vấn cho anh/chị về các ngành học tại trường. Rất vui được hỗ trợ anh/chị hôm nay! Chúc anh/chị một ngày tuyệt vời! 😊")],
        elem_id="chatbot",
        bubble_full_width=False,
        avatar_images=("images/avt_user.png", "images/bot.png"),
    )
    
    with gr.Row():
        txt = gr.Textbox(
            show_label=False,
            placeholder="Nhập tin nhắn của bạn ở đây...",
            elem_id="msg-box"
        )
        submit_btn = gr.Button("Gửi", elem_id="send-btn")
    
    txt.submit(chat_with_history, [txt, chatbot], [txt, chatbot])
    submit_btn.click(chat_with_history, [txt, chatbot], [txt, chatbot])

    with gr.Row(elem_classes="button-row"):
        clear = gr.Button("Xóa tin nhắn", elem_id="clear-btn")
        reset = gr.Button("Reset cuộc trò chuyện", elem_id="reset-btn")

    clear.click(lambda: None, None, chatbot, queue=False)
    reset.click(reset_conversation, outputs=[chatbot, txt])

demo.launch()