from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Provide the correct path to your ChromeDriver
chromedriver_path = 'C:\\Program Files (x86)\\chromedriver.exe'  # Adjust this path as needed
service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver with the Service object
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open the browser in maximized mode
driver = webdriver.Chrome(service=service, options=options)

# Open Instagram
driver.get("https://www.instagram.com/")

# Print the title of the page
print(driver.title)
print("Opened Instagram")

try:
    # Invalid login case
    login_email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "username"))
    )
    login_email.click()
    login_email.clear()
    login_email.send_keys("invalid_user@gmail.com")

    login_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )
    login_password.click()
    login_password.clear()
    login_password.send_keys("InvalidPassword" + Keys.ENTER)

    print("Invalid login attempt executed")

    # Wait for any error message to be displayed
    time.sleep(5)

    # Clear the input fields
    login_email.send_keys(Keys.CONTROL + "a")
    login_email.send_keys(Keys.DELETE)
    login_password.send_keys(Keys.CONTROL + "a")
    login_password.send_keys(Keys.DELETE)

    # Valid login case
    login_email.send_keys("somyasuhani2024")
    login_password.send_keys("Somya@123" + Keys.ENTER)

    print("Valid login attempt executed")

    # Wait for the "Save Info" button to appear
    time.sleep(20)

    # Press TAB key multiple times and then ENTER key
    actions = webdriver.ActionChains(driver)
    for _ in range(1):
        actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Wait a moment to let the action be processed
    time.sleep(8)

    # Press TAB key again and ENTER key
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    print("Clicked 'Save Info' button")

    # Wait for the search button to be clickable
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Search']"))
    )

    # Click the search button
    search_button.click()
    print("Clicked on search button")

    # Wait for the search input field to be visible
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
    )
    time.sleep(5)
    # Enter the search query
    search_query = "darshan raval"
    search_input.send_keys(search_query)
    search_input.send_keys(Keys.ENTER)
    
    # Wait for the results to load and select the first result
    time.sleep(8)
    # Wait for the results to load
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]"))
    )

    # Click the first search result
    first_result.click()

    print(f"Searched for {search_query} and selected the first result")
    
    time.sleep(5)
    
    # follow
    follow = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]')
    follow.click()
    time.sleep(5)
    print("Follow button is clicked")

    time.sleep(5)
    #unfollow=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button')
    #unfollow.click()
    #unfollow_confirm=find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]')
    #time.sleep(15)
    
    # Scroll down to load recent posts
    scroll_pause_time = 2  # Pause time between scrolls
    screen_height = driver.execute_script("return window.innerHeight;")  # Get the screen height

    for i in range(2):  # Number of scrolls; adjust as necessary
        driver.execute_script(f"window.scrollTo(0, {screen_height * (i + 1)});")
        time.sleep(scroll_pause_time)
        
    print("Scrolling screen performed")
    
    time.sleep(5)    
    # Click on the most recent post
    recent_post = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "_aagu"))
    )
    recent_post.click()

    print("Clicked recent post")

    # Wait for the post to load
    time.sleep(8)

    # Like the post
    #like_button = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div"))
    #)    
    #like_button.click()
    #print("Liked the post")
    
    #time.sleep(2)
    
    # Comment on the post

    
    comment = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x78zum5.x1q0g3np.xwib8y2.x1yrsyyn.x1xp8e9x.x13fuv20.x178xt8z.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xo1ph6p.x1pi30zi.x1swvt13 > span:nth-child(2) > div"))
        
    )                                          
    comment.click()
    
    time.sleep(5)
    comment_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x5ur3kl.x13fuv20.x178xt8z.x1roi4f4.x2lah0s.xvs91rp.xl56j7k.x17ydfre.x1n2onr6.x10b6aqq.x1yrsyyn.x1hrcb2b.x1pi30zi > div > form > div > textarea"))
    )
    
    comment_input.send_keys("Great post!")
    comment_input.send_keys(Keys.ENTER)
    print("Commented on the post")

    time.sleep(5)

    #saving post
    save_post= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x78zum5.x1q0g3np.xwib8y2.x1yrsyyn.x1xp8e9x.x13fuv20.x178xt8z.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xo1ph6p.x1pi30zi.x1swvt13 > span.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1rg5ohu.xln7xf2.xk390pu.xdj266r.x1sre0sj.xat24cr.x1gryazu.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf > div > div > div" ))
    )
    save_post.click()
    print("Saved post")

    time.sleep(5)
    #Remove from saved posts
    save_post= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x78zum5.x1q0g3np.xwib8y2.x1yrsyyn.x1xp8e9x.x13fuv20.x178xt8z.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xo1ph6p.x1pi30zi.x1swvt13 > span.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1rg5ohu.xln7xf2.xk390pu.xdj266r.x1sre0sj.xat24cr.x1gryazu.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf > div > div > div" ))
    )
    save_post.click()
    print("Removed from saved posts")
    
    #like comments
    #comment_like = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div[3]/div/div/div[1]/ul/div/li/div/span/div"))
    #)                                          
    #comment_like.click()
    #print("liked comment")

    time.sleep(5)
    #closing post by clicking cross
    
    cross_button= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm > div"))
    )                                          
    cross_button.click()
    print("Clicked cross button to close post")
    
    #going on reels section
    reels_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Reels']"))
    )               
    reels_section.click()
    print("Reels")

    # Scroll through reels using arrow keys
    time.sleep(5)  # Wait for reels to load
    actions = webdriver.ActionChains(driver)
    
    # Scroll down with the DOWN arrow key
    for _ in range(5):  # Adjust the range as needed
        actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)  # Adjust the pause time as needed

    print("Scrolled Down reels with arrow key")
    
    # Scroll up with the UP arrow key
    for _ in range(5):  # Adjust the range as needed
        actions.send_keys(Keys.ARROW_UP).perform()
        time.sleep(2)  # Adjust the pause time as needed

    print("Scrolled up reels with arrow keys")

    #like Reels
    #reel_like = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Like']"))
    #)                                          
    #reel_like.click()
    #reel_like.click()
    #print("liked Reel")
    #print("Disliked Reel")

    time.sleep(5)
    #comment on reel
    #reel_comment = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div[2]/div/div"))
    #)                                          
    #reel_comment.click()
    
    #comment_write = WebDriverWait(driver, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/p"))
    #)                                          
    #comment_write.click()
    #comment_write.send_keys("Great post!")
    #comment_write.send_keys(Keys.ENTER)
    #print("Commented on the reel")



    
    #going to message section
    message = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Messenger']"))
    )                                          
    message.click()
    print("going to msg section")

    time.sleep(3)
    #Opening a chat
    chat = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div"))
    )                                          
    chat.click()
    print("Opened a chat")

    
    
        

except Exception as e:
    print(f"Input element not found or not interactable: {e}")

  

# Wait for a few seconds (adjust as necessary)
#time.sleep(5)

# Quit the WebDriver
#driver.quit()
