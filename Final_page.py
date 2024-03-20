import streamlit as st
import os
from PIL import Image



st.set_page_config(page_title="Tree Trends",layout='wide')#To change the page layout

selected_path=os.getcwd()

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)





#########                   Header Section                       #####################
header_style = "font-size: 17px; text-transform: uppercase; font-weight: bold;"
header = st.columns(13)
with header[0]:
    st.image(Image.open(os.getcwd()+ f"\Recommended\Logo\Logo.png"), width=50)
with header[1]:
    st.markdown(f"<div style='{header_style}'>TREE&nbspTRENDS</div>", unsafe_allow_html=True)
with header[10]:
    st.markdown(":hamster: LOG IN")
with header[11]:
    st.markdown(":white_heart: WISHLIST")
with header[12]:
    st.markdown(":shopping_trolley: CART")

headers = ["Men", "Women", "Jeans", "Sale"]
for idx, header_text in enumerate(headers, start=3):
    with header[idx]:
        st.write(header_text)

header2=st.columns(3)
with header2[1]:
    search_query = st.text_input(label="search",key="search_query",placeholder="Search", label_visibility='collapsed', max_chars=None)
    


st.write("---")




def upper():
    filtered_columns=st.columns(7)
    with filtered_columns[0]:
        gender = st.multiselect(label="Gender",options=["All", "Men", "Women", "Kids"], placeholder="Gender", label_visibility="collapsed")
    with filtered_columns[1]:
        category = st.multiselect(label="Category", options=["All", "Shirts", "Pants", "Shoes", "Accessories"], placeholder="Category", label_visibility="collapsed")
    with filtered_columns[2]:
        sizes = st.multiselect(label="Sizes", options=["S", "M", "L", "XL", "XXL"], placeholder="Size", label_visibility="collapsed")
    with filtered_columns[3]:
        price_range = st.multiselect(label="Price Range", options=["1-1000", "1001-2000", "2001-3000", "3001-4000", "4001-5000"], placeholder="Price Range(in ₹)", label_visibility="collapsed")
    with filtered_columns[4]:
        color = st.multiselect(label="Color", options=["All", "Red", "Blue", "Green", "Black", "White"], placeholder="Color", label_visibility="collapsed")
    with filtered_columns[6]:
        sort_by = st.multiselect(label="Sort by", options=["Relevance", "Price Low to High", "Price High to Low", "Rating"], placeholder="Sort By", label_visibility="collapsed")



    selected_filters = f"<span style='font-size: 18px;'><b>Gender:</b></span> {', '.join(gender) if gender else 'All'} &nbsp;&nbsp;&nbsp;&nbsp;| <span style='font-size: 18px;'><b>Category:</b></span> {', '.join(category) if category else 'All'} &nbsp;&nbsp;&nbsp;&nbsp;| <span style='font-size: 18px;'><b>Sizes:</b></span> {', '.join(sizes) if sizes else 'All'} &nbsp;&nbsp;&nbsp;&nbsp;| <span style='font-size: 18px;'><b>Price Range(in ₹):</b></span> {', '.join(price_range) if price_range else 'All'} &nbsp;&nbsp;&nbsp;&nbsp;| <span style='font-size: 18px;'><b>Color:</b></span> {', '.join(color) if color else 'All'} &nbsp;&nbsp;&nbsp;&nbsp;| <span style='font-size: 18px;'><b>Sort By:</b></span> {', '.join(sort_by) if sort_by else 'All'}"
    st.write(selected_filters, unsafe_allow_html=True)





################               Home Page               #################
def homepage():
    pick_path= selected_path + f"\Recommended\default"
    img_urls = [pick_path + "\\" + f for f in os.listdir(pick_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    button1 = col3.button("MEN", key="button1")
    button2 = col4.button("WOMEN")

    columns = st.columns(5)

    def show_images(img_urls, img_name, img_price):
        for i in range(5):
            with columns[i]:
                st.image(Image.open(img_urls[i]))
                st.write(f'{img_name[i]} <br>**{img_price[i]}**', unsafe_allow_html=True)



    card_cols = st.columns(5)
    card_placeholders = [col.empty() for col in card_cols]
    text_columns = st.columns(5)
    text_placeholders = [col.empty() for col in text_columns]

    def clear_images():
        for i in range(5):
            text_placeholders[i].empty()
            card_placeholders[i].empty()



    #Default Images
    def_img_path= selected_path + f"\Recommended\default"
    img_urls = [def_img_path + "\\" + f for f in os.listdir(def_img_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    def_img_name=['Women Cargo', 'Women Top', 'Men Black Shirt', 'Men Blue Shorts', 'Men Check Shirts']
    def_price = ['₹2,999','₹1,199','₹1,549','₹1,999','₹2,399']
    for i in range(5):
        card_placeholders[i].image(Image.open(img_urls[i]))
        text_placeholders[i].write(f'{def_img_name[i]}<br> **{def_price[i]}**', unsafe_allow_html=True)



    #Men Images
    men_path= selected_path + f"\Recommended\men"
    men_img_urls = [men_path + "\\" + f for f in os.listdir(men_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    men_img_name=['Pink Faded Tshirt', "Plain White Tshirt", "Checked Shirt", "White Shorts", "Blue Jeans"]
    men_price=["₹999", "₹699", "₹1,799", "₹1,299", "₹2,299"]

    if button1:
        clear_images()
        show_images(men_img_urls, men_img_name, men_price)



    #Women Images
    women_path= selected_path + f"\Recommended\women"
    women_img_urls = [women_path + "\\" + f for f in os.listdir(women_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    women_img_name=["Brown Kurti", "Floral Top", "Black Jeans", "Blue Jeans", "White Jeans"]
    women_price=["₹1,299", "₹899", "₹2,299", "₹2,999", "₹2,499"]

    if button2:
        clear_images()
        show_images(women_img_urls, women_img_name, women_price)



    ###Recommend section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align:center;font-size:24px;font-weight:bold;margin-bottom:20px'>Trending Styles!</div>",
        unsafe_allow_html=True
    )

    rec_main_path= selected_path + f"\Recommended\Random"
    rec_main_urls = [rec_main_path + "\\" + f for f in os.listdir(rec_main_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    rec_img_name=["Yellow Checked Shirt", "White Shirt", "Light Blue Jeans", "Black Checked Top", "White Jeans Women"]
    rec_price=["₹1,899", "₹2,049", "₹2,799", "₹1,299", "₹2,799"]

    rColumns = st.columns(5)
    

    for i in range(5):
        with rColumns[i]:
            with Image.open(rec_main_urls[i]) as img:
                img = img.resize((300,350))
                st.image(img)
                st.write(f'{rec_img_name[i]}<br>**{rec_price[i]}**', unsafe_allow_html=True)





# Function to display content for shirts
def shirts_page():
    vanish=st.empty()
    home=vanish.button(':back: Home')
    if home:
        vanish.empty()
        homepage()
        return
    #########             Search results for tshirts            #####################
    st.title("Results for Tshirts")



    # In page option to show the filters
    upper()
    


    # #########             Content of the Website(Display, Recommend)            #####################
    pick_path= selected_path + f"\Recommended\shirts"
    uploaded_files = [pick_path + "\\" + f for f in os.listdir(pick_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

    sel_men_shirt=['Grey Polo Tshirt', 'Pink Plain Tee', 'Pink Faded Tee', 'Mens Polo', 'Plain Grey Tee']
    sel_men_shirt_price = ['₹1,199','₹699','₹849','₹999','₹599']
    recommended_images_dict = {}
    recommended_imgs_list = {'1.png': '1r', '2.png': '2r', '3.png': '3r', '4.png': '4r', '5.png': '5r'} #A recommended images folder is created for each photo
    complete_images_dict = {}
    complete_imgs_list = {'1.png': '1c', '2.png': '2c', '3.png': '3c', '4.png': '4c', '5.png': '5c'}
    rec_men_shirt = {
        0: ['Light Grey Tee', 'Navy Blue Tee', 'Grey Stripes Polo', 'Black Collar Polo', 'Coin Grey Polo'],
        1: ['Maroon Polo', 'Pink Polo', 'Peach Polo', 'Mint Green Polo'],
        2: ['Pink Designed Tee', 'Light Pink Faded Tee', 'Light Blue Faded Tee'],
        3: ['Black Stripes Polo', 'Grey-Blue Stripes Polo', 'Black&Brown Polo', 'White Polo'],
        4: ['Black Stripes Tee', 'Printed Tee', 'Light Green Faded Tee', 'Plain Blue Tee']
    }
    rec_men_shirt_price = {
        0: ['₹1,299', '₹1,199', '₹1,499', '₹1,399', '₹999'],
        1: ['₹1,199', '₹1,199', '₹1,199', '₹1,199'],
        2: ['₹1,099', '₹899', '₹999'],
        3: ['₹1,199', '₹1,199', '₹1,299', '₹1,399'],
        4: ['₹799', '₹999', '₹849', '₹599']
    }
    
    images_per_row = 5

    st.markdown("<span style='font-size:18px; font-style: italic;'>5 items found</span>",unsafe_allow_html=True)
    selected_images_col = st.columns(images_per_row)

    # To show the selected images
    for idx, file in enumerate(uploaded_files):
        file_name = os.path.basename(file)
        with Image.open(file) as img:
            img = img.resize((300, 350))
            selected_images_col[idx % images_per_row].image(img, use_column_width=True)
            selected_images_col[idx].write(f'{sel_men_shirt[idx]} <br>**{sel_men_shirt_price[idx]}**', unsafe_allow_html=True)


        
        recommended_button_label = "Recommend"
        complete_button_label = "Complete the look"

        # Recommend button
        if selected_images_col[(idx) % images_per_row].button(recommended_button_label, key={file_name}):
            
            if file_name in recommended_imgs_list:
                data_path= os.getcwd()
                recommended_images_path = data_path + f"\Recommended\shirts\{recommended_imgs_list[file_name]}"
                recommended_image_files = os.listdir(recommended_images_path)

                if recommended_image_files:
                    st.subheader(f"Recommended product")
                            
                    recommended_images_dict[file_name] = recommended_image_files
                    recommended_images_col = st.columns(images_per_row)

                    #Displaying recommended images
                    for rec_idx, recommended_image_file in enumerate(recommended_image_files):
                        recommended_image_path = os.path.join(recommended_images_path, recommended_image_file)

                        with Image.open(recommended_image_path) as img:
                            img = img.resize((300,350))

                            recommended_images_col[rec_idx % images_per_row].image(img)
                            recommended_images_col[rec_idx].write(f'{rec_men_shirt[idx][rec_idx]} <br>**{rec_men_shirt_price[idx][rec_idx]}**', unsafe_allow_html=True)

                                

        if selected_images_col[(idx) % images_per_row].button(complete_button_label, key=f"complete_{file_name}"):
            if file_name in complete_imgs_list:
                data_path= os.getcwd()
                complete_images_path = data_path + f"\Recommended\shirts\{complete_imgs_list[file_name]}"
                complete_image_files = os.listdir(complete_images_path)
                if complete_image_files:
                    st.subheader(f"Styling Ideas")
                    complete_images_dict[file_name] = complete_image_files
                    complete_images_col = st.columns(images_per_row)

                    #Displaying complete images
                    for com_idx, complete_image_file in enumerate(complete_image_files):
                        complete_image_path = os.path.join(complete_images_path, complete_image_file)
                        with Image.open(complete_image_path) as img:
                            img = img.resize((300, 300))
                            complete_images_col[com_idx % images_per_row].image(img)





# Function to display content for pants
def trousers_page():
    vanish=st.empty()
    home=vanish.button(':back: Home')
    if home:
        vanish.empty()
        homepage()
        return
    #########             Search results for pants            #####################
    st.title("Results for Trousers")



    # In page option to show the filters
    upper()



    # #########             Main Content of the Website(Browse, Display, Recommend)            #####################
    pick_path= selected_path + f"\Recommended\pants"
    uploaded_files = [pick_path + "\\" + f for f in os.listdir(pick_path) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

    sel_men_trouser=['Beige Trouser', 'Orange Trouser', 'Grey Formal Pant', 'Blue Jeans', 'Green Trouser']
    sel_men_trouser_price = ['₹2,299','₹1,799','₹2,799','₹2,399','₹1,999']
    recommended_images_dict = {}
    recommended_imgs_list = {'1.png': '1r', '2.png': '2r', '3.png': '3r', '4.png': '4r', '5.png': '5r'} #A recommended images folder is created for each photo
    complete_images_dict = {}
    complete_imgs_list = {'1.png': '1c', '2.png': '2c', '3.png': '3c', '4.png': '4c', '5.png': '5c'}
    rec_men_trouser = {
        0: ['Beige Formal Pant', 'Light Beige Trouser', 'Brown Cargo', 'Off White Trouser', 'Brown Trouser'],
        1: ['Maroon Trouser', 'Maroon Cargo', 'Plain Trouser', 'Straight Fit Cargo', 'Orange Joggers'],
        2: ['Charcoal Grey Trouser ', 'Charcoal Grey Formal Pant', 'Black Jeans', 'Relaxed Fit Jeans', 'Straight Fit Jeans'],
        3: ['Light Blue Cargo', 'Dark Blue Jeans', 'Blue Faded Jeans', 'Relaxed Fit Jeans', 'Blue Stylish Jeans'],
        4: ['Straight Fit Trouser', 'Carrot Fit Trouser', 'Mint Green Trouser', 'Green Joggers', 'Camouflaged Trouser']
    }
    rec_men_trouser_price = {
        0: ['₹1,299', '₹1,199', '₹1,499', '₹1,399', '₹999'],
        1: ['₹1,899', '₹2,199', '₹1,799', '₹1,799', '₹1,299'],
        2: ['₹1,999', '₹2,799', '₹2,299', '₹2,099', '₹1,999'],
        3: ['₹2,199', '₹2,499', '₹2,299', '₹1,999', '₹2,299'],
        4: ['₹1,799', '₹1,999', '₹1,849', '₹1,299', '₹2,099']
    }

    recommended_image_width = 300
    recommended_image_height = 350
    images_per_row = 5 

    st.markdown("<span style='font-size:18px; font-style: italic;'>5 items found</span>",unsafe_allow_html=True)
    selected_images_col = st.columns(images_per_row)

    # To show the selected images
    for idx, file in enumerate(uploaded_files):
        file_name = os.path.basename(file)
        with Image.open(file) as img:
            img = img.resize((recommended_image_width, recommended_image_height))
            selected_images_col[idx % images_per_row].image(img, use_column_width=True)
            selected_images_col[idx].write(f'{sel_men_trouser[idx]} <br>**{sel_men_trouser_price[idx]}**', unsafe_allow_html=True)
        
        recommended_button_label = "Recommend"
        complete_button_label = "Complete the look"

        # Recommend button
        if selected_images_col[(idx) % images_per_row].button(recommended_button_label, key={file_name}):
            if file_name in recommended_imgs_list:
                data_path= os.getcwd()
                recommended_images_path = data_path + f"\Recommended\pants\{recommended_imgs_list[file_name]}"
                recommended_image_files = os.listdir(recommended_images_path)

                if recommended_image_files:
                    st.subheader(f"Recommended products")
                            
                    recommended_images_dict[file_name] = recommended_image_files
                    recommended_images_col = st.columns(images_per_row)

                    #Displaying recommended images
                    for rec_idx, recommended_image_file in enumerate(recommended_image_files):
                        recommended_image_path = os.path.join(recommended_images_path, recommended_image_file)

                        with Image.open(recommended_image_path) as img:
                            img = img.resize((300,350))
                            recommended_images_col[rec_idx % images_per_row].image(img)
                            recommended_images_col[rec_idx].write(f'{rec_men_trouser[idx % images_per_row][rec_idx % images_per_row]} <br>**{rec_men_trouser_price[idx % images_per_row][rec_idx % images_per_row]}**', unsafe_allow_html=True)


                                

        if selected_images_col[(idx) % images_per_row].button(complete_button_label, key=f"complete_{file_name}"):
            if file_name in complete_imgs_list:
                data_path= os.getcwd()
                complete_images_path = data_path + f"\Recommended\pants\{complete_imgs_list[file_name]}"
                complete_image_files = os.listdir(complete_images_path)
                if complete_image_files:
                    st.subheader(f"Syling Ideas")
                    complete_images_dict[file_name] = complete_image_files
                    complete_images_col = st.columns(images_per_row)

                    #Displaying complete images
                    for com_idx, complete_image_file in enumerate(complete_image_files):
                        complete_image_path = os.path.join(complete_images_path, complete_image_file)
                        with Image.open(complete_image_path) as img:
                            img = img.resize((300,300))
                            complete_images_col[com_idx % images_per_row].image(img)
                            # complete_images_col[com_idx % images_per_row].button(label="Add to Cart", key={complete_image_file}):





# If searched product is not found
def wrong():
    vanish=st.empty()
    home=vanish.button(':back: Home')
    if home:
        vanish.empty()
        homepage()
        return
    
    st.title("Items not found!")

    st.subheader("Try searching for Tshirts or Trousers")





# Define the content area
if search_query:
    if search_query.lower() == "tshirts" or search_query.lower() == "tshirt" or search_query.lower() == "t-shirts" or search_query.lower() == "t-shirt":
        shirts_page()  # Display shirts content
    elif search_query.lower() == "trousers" or search_query.lower() == "trouser":
        trousers_page()  # Display pants content
    else:
        wrong()  # Display the warning
else:
    homepage()  # Display the homepage by default





# ############                   Footer section             #####################
# Footer Section
st.write("---")  # A horizontal line to separate the content

footer_div = """
    <section class = "contactus", id = "contact">
        <div style="background-color: #f0f0f0; padding: 20px;">
            <div style="max-width: 100vw; margin: 0 auto;padding:10px">
                <hr style="border-top: 1px solid #ccc;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style = "height:45vh;font-size:1.2rem">
                        <h4>Contact Us:</h4>
                        <p><span style='font-size:20px; font-style: bold;'>Email:</span><span style='font-size:18px;'> info@tredence.com</span></p>
                        <p><span style='font-size:20px; font-style: bold;'>Address:</span><span style='font-size:18px;'> <br>2nd Floor, Office 2, Wing B, Sattva Knowledge Court,<br> Plot No. 9 of Doddenakkundi I Phase Industrial Area,<br> Doddenakkundi Village, Hobli, Krishnarajapura,<br> Bengaluru, Karnataka 560048</span></p>
                        <p><span style='font-size:20px; font-style: bold;'>Phone:<span style='font-size:18px;'> +91-80-61561000</span></p>
                    </div>
                    <div style = "height:40vh;font-size:1.2rem">
                        <h4>Follow Us:</h5>
                        <a href="https://www.linkedin.com/company/tredence" target="_blank"><span style='font-size:22px;'>LinkedIn</a></span><br>
                        <a href="https://twitter.com/yourpage" target="_blank"><span style='font-size:22px;'>Twitter</a></span><br>
                        <a href="https://www.instagram.com/tredenceinc" target="_blank"><span style='font-size:22px;'>Instagram</span></a>
                    </div>
                </div>
                <p style="text-align: center; margin-top: 60px;">© 2023 Tredence Inc. All rights reserved.</p>
            </div>
        </div>
    </section>
"""
st.markdown(footer_div, unsafe_allow_html=True)