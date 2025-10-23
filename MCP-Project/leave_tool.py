from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
load_dotenv()
def apply_leave(start_day: str, end_day: str) -> str:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        url =os.getenv("LEAVE_URL")
        USER_NAME =os.getenv("USER_NAME")
        USER_PASSWORD =os.getenv("USER_PASSWORD")
        # Login page
        print(f'${url}${USER_NAME}')
        page.goto(url)
        page.get_by_role("textbox", name="Login ID").fill(USER_NAME)
        page.get_by_role("textbox", name="Password").fill(USER_PASSWORD)
        page.get_by_role("button", name="Login").click()

        # Navigate to Leave Apply
        leave_apply_path = "/leave/leave-workflow/apply/leave"
        page.wait_for_url("**/home", timeout=20000)
        leave_apply_url = page.url.replace("/home", leave_apply_path)
        page.goto(leave_apply_url)

        # Select leave type
        page.get_by_role("button", name="Select type").click()
        page.get_by_role("link", name="Casual Leave").click()

        # Select start date
        page.locator("gt-leave-date-picker[name='fromDate'] button").click()
        page.wait_for_selector(".gt-leave-date-picker-calendar", state="visible")
        page.get_by_role("cell", name=start_day).locator("div").first.click()

        # Select end date
        page.locator("gt-leave-date-picker[name='toDate'] button").click()
        page.get_by_role("cell", name=end_day).locator("div").first.click()



        # Submit
        # page.get_by_role("button", name="Submit").click()
        print(f"✅ Leave applied from {start_day} to {end_day}")

        page.wait_for_timeout(5000)
        context.close()
        browser.close()
        return "successfully applied leave"
