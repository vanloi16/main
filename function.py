import requests
import json
import os
import sys
import time
import base64, random
import re
import uuid
from io import BytesIO
red = "\033[1;91m"
vang = "\033[1;93m"
luc = "\033[1;92m"
trang = "\033[1;97m"
tim = "\033[1;95m"
lam = "\033[1;96m"
xduong = "\033[1;94m"
daucau = f"{red}[{vang}•{red}]{trang} >> "
def cls():
	return os.system('cls' if os.name == 'nt' else 'clear')
def thanhngang():
	print(red+"-"*50)
def See():
	return sys.exit(red+"See You")
def b64enc(arg):
	return base64.b64encode(arg.encode('utf-8')).decode('utf-8')

time_file = "time_showprofile.txt"
def get_current_time():
	return time.time()

def write_time_to_file():
	future_time = get_current_time() + 120
	with open(time_file, "w") as f:
		f.write(str(future_time))
def check_login_time():
	if os.path.exists(time_file):
		with open(time_file, "r") as f:
			login_time = float(f.read().strip())
		current_time = get_current_time()
		if current_time >= login_time:
			return True
		else:
			wait_time = login_time - current_time
			print(f"{trang}Vui lòng chờ {vang}{wait_time:.2f} {trang}giây nữa, để tiếp tục", end="\r")
			return False
	return True
def login():
	while True:
		if check_login_time():
			write_time_to_file()
			break
			
		else:pass
#delay job tds
def DELAY(seconds):
	huhu = [red, vang, lam, trang, luc, tim]
	for i in range(seconds, -1, -1):
		sys.stdout.write("\r")
		sys.stdout.write(f"{random.choice(huhu)}Vui Lòng Đợi Sau {i} Giây    ")
		sys.stdout.write("\r")
		time.sleep(1)
	print(" "*50, end="\r")
	sys.stdout.flush()

def Hide_ID(id):
	old = id[:13]
	new = old[:6].ljust(len(old), "#")
	return new

def current_time():
	from datetime import datetime
	now = datetime.now()
	return now.strftime("%H:%M:%S")
ho_list = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Huỳnh', 'Phan', 'Vũ', 'Võ', 'Đặng', 'Bùi', 'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Lý']
dem_list = ['Văn', 'Thị', 'Hữu', 'Đức', 'Minh', 'Xuân', 'Ngọc', 'Hải', 'Thanh', 'Anh', 'Bảo', 'Gia', 'Trọng', 'Quang', 'Phúc']
ten_list = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hồ', 'Huỳnh', 'Hoàng', 'Phan', 'Vũ', 'Võ', 'Đặng', 'Bùi', 'Đỗ', 'Hứa', 'Lý', 'Cao', 'Đinh', 'Doãn', 'Đào', 'Đức', 'Dương', 'Giang', 'Hà', 'Hàn', 'Khuất', 'Khương', 'La', 'Lâm', 'Lục', 'Mai', 'Mạc', 'Nghê', 'Nghiêm', 'Ngo', 'Ngô', 'Nguyên', 'Phó', 'Quách', 'Quang', 'Quản', 'Quý', 'Tạ', 'Thái', 'Thạch', 'Thân', 'Thang', 'Thảo', 'Thi', 'Thích', 'Thịnh', 'Thôi', 'Tiêu', 'Tô', 'Trang', 'Trình', 'Trịnh', 'Trương', 'Từ', 'Ung', 'Viên', 'Vương', 'Vưu', 'Yên', 'Văn', 'Thị', 'Đình', 'Minh', 'Ngọc', 'Hữu', 'Thanh', 'Bảo', 'Anh', 'Kim', 'Thế', 'Duy', 'Thu', 'Tú', 'Phúc', 'Khắc', 'Bá', 'Thúy', 'Quốc', 'Trung', 'Hùng', 'Việt', 'Tấn', 'Trường', 'Kỳ', 'Phương', 'Nhật', 'Quyền', 'Hạnh', 'Hiền', 'Hải', 'Nam', 'Tuấn', 'Công', 'Đăng', 'Xuân', 'Đại', 'Mạnh', 'Đoàn', 'Chi', 'Lệ', 'Tường', 'Vi', 'Dũng', 'Linh', 'Thuỷ', 'Thắng', 'Quân', 'Tùng', 'Vân', 'Khánh', 'Trinh', 'Bình', 'Hoa', 'Phú', 'Phong', 'Lộc', 'Đạt', 'Thành', 'Huy', 'Khoa', 'Tuyết', 'Lan', 'Ngân', 'Huyền', 'Nhung', 'Thụy', 'Hương', 'Sơn', 'Bích', 'Thắm', 'Trúc', 'Hảo', 'Nga', 'Tiến', 'Tâm', 'Vinh', 'Tân', 'Uyên', 'Châu', 'Thúc', 'Trâm', 'Diệp', 'Hồng', 'Long', 'Nhi', 'Trân', 'Hiệu', 'Khải', 'An', 'Hào', 'Tiên', 'Kiệt', 'Diệu', 'Thông', 'Hiệp', 'Diễm', 'Thoa', 'Tiệp', 'Bách', 'Tính', 'Thục', 'Hiển', 'Đoan', 'Sĩ', 'Chính', 'Tuyến', 'Triệu', 'Khang', 'Nghĩa', 'Hòa', 'Bằng', 'Khuê', 'Quyên', 'Dung', 'Yến', 'Phấn', 'Thạc', 'Hàm', 'Hân', 'Nguyệt', 'Tình', 'Thường', 'Hiên', 'Tín', 'Thụ', 'Chương', 'Tuyền', 'Hiếu', 'Nghị', 'Thùy', 'Nhiên', 'Phượng', 'Huệ', 'Thuần', 'Phụng', 'Như', 'Đan', 'Ánh', 'Duyên', 'Điệp', 'Nhã', 'Thơ', 'Oanh', 'Đài', 'Hạ', 'Nhàn', 'Thủy', 'Hạc', 'Nghi', 'Hằng', 'Dạ', 'Thơm', 'Phước', 'Đông', 'Vĩnh', 'Hưng', 'Trí', 'Trọng', 'Kiên', 'Khôi', 'Vĩ', 'Mỹ', 'Quỳnh', 'Gia', 'Cẩm', 'Bạch', 'Ân']

def generate_vietnamese_name():
	ho = random.choice(ho_list)
	dem = random.choice(dem_list)
	ten = random.choice(ten_list)
	return str(f"{ho} {dem} {ten}")

class API_TDS:
	def __init__(self, token):
		self.token = token
		self.headers = {'Host': 'traodoisub.com', 'cache-control': 'max-age=0', 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6'}
	def login(self):
		url_login = f"https://traodoisub.com/api/?fields=profile&access_token={self.token}"
		try:
			request_to_url_login = requests.get(url_login, headers=self.headers)
			request_to_url_login.raise_for_status()
			return request_to_url_login.json()
		except Exception as msg:
			print(msg)
		return False
	def config(self, idfb):
		url_config = f"https://traodoisub.com/api/?fields=run&id={idfb}&access_token={self.token}"
		try:
			request_to_url_config = requests.get(url_config, headers=self.headers)
			request_to_url_config.raise_for_status()
			return request_to_url_config.json()
		except Exception:
			pass
		return False
	def getjob(self, type, type2="ALL"):
		if type == "likesieure":
			self.type=type 
		elif type == "comment":
			self.type=type
		elif type == "share":
			self.type = type
		elif type == "follow":
			self.type = f"facebook_{type}"
		elif type == "reaction":
			self.type = type
		elif type == "reactcmt":
			self.type = type
		elif type == "page":
			self.type = f"facebook_{type}"
		elif type == "group":
			self.type = type
		if type == "share":
			url_getjob = f"https://traodoisub.com/api/?fields={self.type}&access_token={self.token}"
		else:
			url_getjob = f"https://traodoisub.com/api/?fields={self.type}&access_token={self.token}&type={type2}"
		try:
			with requests.get(url_getjob, headers=self.headers) as request_to_getjob:
				request_to_getjob.raise_for_status()
				return request_to_getjob
		except Exception:
			pass
		return False
	def postjob(self, utype, code):
		if utype == "follow":
			type = "facebook_follow_cache"
		else:
			type = "facebook_page_cache"
		try:
			url_postjob = f"https://traodoisub.com/api/coin/?type={type}&id={code}&access_token={self.token}"
			request_post_coin = requests.get(url_postjob, headers=self.headers)
			request_post_coin.raise_for_status()
			return request_post_coin.json()
		except Exception:...
		return False
	def getcoin_api_old(self, type, id):
		url_getcoin = f"https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}"
		try:
			request_coin = requests.get(url_getcoin, headers=self.headers)
			request_coin.raise_for_status()
			return request_coin
		except Exception as msg:...
		return False
			
	def getcoin_api_new(self, type, id): # continue...
		if type == "share":
			self.type = "facebook_share"
			id=id
		elif type == "follow":
			self.type = "facebook_follow"
			id="facebook_api"
		elif type == "page":
			self.type = "facebook_page"
			id="facebook_api"
		
		url_getcoin = f"https://traodoisub.com/api/coin/?type={self.type}&id={id}&access_token={self.token}"
	#	print(url_getcoin)
		try:
			request_coin = requests.get(url_getcoin, headers=self.headers)
			request_coin.raise_for_status()
			return request_coin
		except Exception as msg:
			...
		return False
class API_FACEBOOK:
	def __init__(self):
		self.url_image = ['https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GV5PK4ZW0AA6-Jp.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GV5PK4pWYAASE1p.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GcaenoLWMAEd_WP.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GcaenoSX0AAhFDc.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GcaenoTWkAAZatr.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcbs_0HXgAAYoa9.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcbs_0TXwAAUzt_.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcbs_0UXIAAMwPJ.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcc9eolWsAAOtyo.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcc9eonXIAAovox.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcc9eonXgAAxlDQ.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gccb8QUXkAAZasY.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gccb8QZWMAAF-OW.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gccb8QZXUAAxoQH.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcd9ZDDXoAAAHai.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcd9ZDIXQAAc0ak.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcd9ZFGXMAAarlt.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GcgHrxXWoAAQ0a8.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GcgHrxeXUAAR-5-.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GcgHrxkWQAEwlTP.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcgkg06WIAAPbL5.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcgkg07X0AAR-Jl.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gcgkg08WUAA25tB.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GchpdoaW4AAyqnQ.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GchpdouXwAA-pB7.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gci6DE1XwAEAJim.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gci6DFJXQAABIrU.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_Gci6DFKWMAABGGy.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GciSAMxWgAAz_G0.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GciSANEWAAA1HNA.jpg', 'https://raw.githubusercontent.com/vanloi16/Public_Image_Page/main/SaveTwitter.Net_GciSANHXcAAqHhj.jpg']
		self.url = "https://www.facebook.com/api/graphql/"
		self.headers = {'Host': 'www.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate', 'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': ''}
		self.h2 = {'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 'cache-control': 'no-cache', 'cookie': '', 'pragma': 'no-cache', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'}
	def getdata(self, cookie):
		url_fb = "https://www.facebook.com/friends"
		self.headers['cookie'] = cookie
		try:
			obj = r'c_user=(\d+);'
			object_idfb = re.findall(obj, cookie)[0]
			with requests.get(url_fb, headers=self.headers) as request_data:
				request_data.raise_for_status()
		except Exception as msg:
			return False
		object_data = request_data.text
		try:
			fb1, fb2, spin_r, spin_t, hsi, lsd = [re.search(x, object_data).group(1) for x in [
				r'\["DTSGInitialData",\[\],\{"token":"(.*?)"',
				r'15&jazoest=(.*?)"',
				r'"__spin_r":(.*?),',
				r'"__spin_t":(.*?),',
				r',"hsi":"(.*?)"',
				r'\["LSD",\[\],\{"token":"(.*?)"']]
			name = re.search(r'"User","id":"' + object_idfb + '","name":"(.*?)"', object_data)
			return fb1, fb2, spin_r, spin_t, hsi, lsd, name.group(1).encode('utf-8').decode('unicode_escape'), object_idfb
		except Exception as msg:
			return False
	def Bypass_CheckPoint(self, fb1, fb2, cookie):
		data_bypass = {"jazoest": fb1, "fb_dtsg": fb2}
		try:
			self.headers['cookie'] = cookie
			with requests.post("https://www.facebook.com/checkpoint/601051028565049/submit/", headers=self.headers, data=data_bypass) as request_bypass:
				request_bypass.raise_for_status()
				return True
		except Exception:...
		return False
			
	def RegProfile(self, idfb, hsi, fb1, fb2, lsd, s1, s2, cookie):
		NAME = generate_vietnamese_name()
		data_reg = {'av': idfb,'__usid': '6-Tsn1tv01xaj3q4:Psn1tumoyp61y:0-Asn1tk1wqz89x-RV=6:F=','__aaid': '0','__user': idfb,'__a': '1','__req': '1c','__hs': '20043.HYP:comet_pkg.2.1..2.1','dpr': '3','__ccg': 'GOOD','__rev': '1018265499','__s': 'uw7pve:z53znf:302qaq','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG0Z82_CxS320qa2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU6a1TxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHwGwbu','__csr': 'gb4AQArff5MEBlisQh7cjh2iRRR8LEuOOkQkN36qbA94ExflOSABFGGEAynqjHmRcKBpl8Z5DJoCyn9AHHGGiOfnF4huuqJmpZUxmWWLmaDx6niUB7jQKQ-ATykE-HDgGHAyoF9uh29F9bDzqGv9rKfUtzUPHCyqyVlV8GfyXxGmi69_JaaK5bjhEjxWECi8AyEeojz8SKm3zxm1rxGF8RonGfDga8cEvwDh88bx27UgWyo4O2e6o2EwJzo4u1kwcO1aK0Ao1Do0xW1ew47wfW2u1twcq05aU8u0mu0K80x-00l3504Sg0Oe095w3MEeU3FwbG0amwmEnwXwmE0j5w32802HKw6Ew0x0w','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"Anh Trai C2","categories":["361282040719868"],"creation_source":"comet","name":"'+NAME+'","off_platform_creator_reachout_id":null,"page_referrer":"comet_home","actor_id":"'+idfb+'","client_mutation_id":"1"}}','server_timestamps': 'true','doc_id': '8146768482082105'}
		try:
			self.headers['cookie'] = cookie
			with requests.post(self.url, headers=self.headers, data=data_reg) as request_reg:
				request_reg.raise_for_status()
				if '"errors"' in request_reg.text:
					return False
				hihi = request_reg.json()
				return {'name': NAME, 'id': hihi['data']['additional_profile_plus_create']['additional_profile']['id']}
		except Exception:...
		return False
	def Up_Avt(self, idfb, hsi, fb1, fb2, lsd, s1, s2, cookie):
		data_avt = {'photo_source': '57','__usid': '6-Tsn1tv01xaj3q4:Psn1tumoyp61y:0-Asn1tk1wqz89x-RV=6:F=','profile_id': idfb,'__aaid': '0','__user': idfb,'__a': '1','__req': '1h','__hs': '20043.HYP:comet_pkg.2.1..2.1','dpr': '3','__ccg': 'GOOD','__rev': '1018265499','__s': 'r9635o:z53znf:302qaq','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG0Z82_CxS320qa2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU6a1TxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHwGwbu','__csr': 'gb4AQArff5MEBlisQh7cjh2iRRR8LEuOOkQkN36qbA94ExflOSABFGGEAynqjHmRcKBpl8Z5DJoCyn9AHHGGiOfnF4huuqJmpZUxmWWLmaDx6niUB7jQKQ-ATykE-HDgGHAyoF9uh4KqiiVUSGDOmXz-7o-cWVECEKluiazUKUqBAxyvXiyHxiQQq4UuG9Ay98G3C4UOdHBwUUlwmUqGidm5WzVQ2y3a7U9Qi22Ugx-4eEC1cwzxC0G8boS17wl83cwiHw960pS08uwjE11U3-wDwno36w1iK27w5Dwby08vw05gNg1dA0czw2ho0Ya3K0Wo2Ww2BE5G5UeU5G04No0My00GXE1G808g8','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2}
		try:
			ahuhu = random.choice(self.url_image)
			get_image = requests.get(ahuhu)
			get_image.raise_for_status()
			content_type = get_image.headers.get('content-type')
			files = {'image': ('image.jpg', BytesIO(get_image.content), content_type)}
			
			self.headers['cookie'] = cookie
			with requests.post("https://www.facebook.com/profile/picture/upload/", headers=self.headers, data=data_avt, files=files) as request_avt:
				request_avt.raise_for_status()
				if '"error"' in request_avt.text:
					return False
				print(request_avt.text)
				return json.loads(request_avt.text[9:])['payload']['fbid']
	
		except Exception as msg:print(str(msg))
		return False
	def Update_AVT(self, idfb, hsi, fb1, fb2, lsd, s1, s2, id_page, cookie, image2):
		data_update = {'av': idfb,'__usid': '6-Tsn1tv01xaj3q4:Psn1tumoyp61y:0-Asn1tk1wqz89x-RV=6:F=','__aaid': '0','__user': idfb,'__a': '1','__req': '1l','__hs': '20043.HYP:comet_pkg.2.1..2.1','dpr': '3','__ccg': 'GOOD','__rev': '1018265499','__s': 'k0o2v7:z53znf:302qaq','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG0Z82_CxS320qa2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU6a1TxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHwGwbu','__csr': 'gb4AQArff5MEBlisQh7cjh2iRRR8LEuOOkQkN36qbA94ExflOSABFGGEAynqjHmRcKBpl8Z5DJoCyn9AHHGGiOfnF4huuqJmpZUxmWWLmaDx6niUB7jQKQ-ATykE-HDgGHAyoF9uh4KqiiVUSGDOmXz-7o-cWVECEKluiazUKUqBAxyvXiyHxiQQq4UuG9Ay98G3C4UOdHBwUUlwmUqGidm5WzVQ2y3a7U9Qi22Ugx-4eEC1cwzxC0G8boS17wl83cwiHw960pS08uwjE11U3-wDwno36w1iK27w5Dwby08vw05gNg1dA0czw2ho0Ya3K0Wo2Ww2BE5G5UeU5G04No0My00GXE1G808g8','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusEditMutation','variables': '{"input":{"additional_profile_plus_id":"'+id_page+'","creation_source":"comet","profile_photo":{"existing_photo_id":"'+image2+'"},"cover_photo":{"existing_cover_photo_id":"'+image2+'","focus":{"x":0.5,"y":0.49983167459646394}},"actor_id":"'+id_page+'","client_mutation_id":"2"}}','server_timestamps': 'true','doc_id': '6470849629597825',}
		
		try:
			print(trang, data_update)
			self.headers['cookie'] = cookie
			request_bonus = requests.post(self.url, headers=self.headers, data=data_update)
			request_bonus.raise_for_status()
			print(request_bonus.json())
			if '"errors"' in request_bonus.text:
				return False
			return True
		except Exception as msg:print(str(msg))
		return False
		
	def ShowPro5(self, idfb, hsi, lsd, s1, s2, cookie, fb1, fb2):
		data_show = {'av': idfb, '__aaid': '0', '__user': idfb, '__a': '1', '__req': '18', '__hs': '20037.HYP:comet_pkg.2.1..2.1', 'dpr': '3', '__ccg': 'GOOD', '__rev': '1018082568', '__s': 'twyw8m:albom3:ugf8co', '__hsi': hsi, '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG0Z82_CxS320qa2OU7m2210wEwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3qxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHweafw', '__csr': 'glhcchcyslll4SGlNklkJgwzRZnbOAl9mAJaD9T8QGFtiO7OYBYJOWbp4AFsT-ylWhHtbLCjDAh5irhmykjkypGpd4p9teX8nAGbWXKqqiXKHtfgOivABHCmUr-jKpGiiRLJy5AUyvhA8hVFAbgkhoJ3pVEK6XCGKfuqqiUSchV8GiFe4WyUOHKEG9z9ENe58jy43y8iAzWBxbDyUrxW8CgC8x279U-icwLwAG265e4EhG3mFQ7EgyGyEhxGi6Gzojwk8lwBAGcxC68vxK2S26ewJwIzES7EdUOrCK1kAz8a8do7W1dwHw-w2bE1k80BO2W0LU4O2K0wU5W9ykcwuE1_83-Bnw6Iw3tku9xbw0hUE0q--00Bzo050t02yQ3q17w3QU0kPBwmo0w208Wwqo0gsw3Bo06uK0bFweqE0f4EdHw9a0ME2Bw1z5wsHaEVwpU2Cwlogg0ye9w', '__comet_req': '15', 'fb_dtsg': fb1, 'jazoest': fb2, 'lsd': lsd,'__spin_r': s1, '__spin_b': 'trunk', '__spin_t': s2, '__jssesw': '1', 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'PageCometLaunchpointLeftNavMenuRootQuery', 'variables': '{"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}', 'server_timestamps': 'true', 'doc_id': '7469722579793405'}
		self.headers['cookie'] = cookie
		self.Bypass_CheckPoint(fb1, fb2, cookie)
		try:
			with requests.post(self.url, headers=self.headers, data=data_show) as request_show_pro5:
				request_show_pro5.raise_for_status()
				ahihi = request_show_pro5.json()
				return ahihi['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
		except Exception:
			...
		return False

	def Like(self, id_page, fb1, fb2, idjob, type, lsd, s1, s2, hsi, cookie):
		self.Bypass_CheckPoint(fb1, fb2, cookie)
		idtype = {'LIKE': '1635855486666999', 'LOVE': '1678524932434102', 'CARE': '613557422527858', 'HAHA': '115940658764963', 'WOW': '478547315650144', 'SAD': '908563459236466', 'ANGRY': '444813342392137'}
		data_like = {'av': id_page, '__aaid': '0', '__user': id_page, '__a': '1','__req': '13','__hs': '20039.HYP:comet_pkg.2.1..0.1','dpr': '3','__ccg': 'EXCELLENT','__rev': '1018119355','__s': '2yzy5b:p8xux3:6yijzk','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K360CEboG0x8bo6u3y4o2Gwn82nwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wSU8o4Wm7-2K0-obXCwLyESE2KwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWzUfHDzUiwRK6E4-mEbUaU3yw','__csr': 'gfsIeMR1x4igDYtczEOdvYQt2JSyOkDfRsQGZR9W5eDOFbGxa9LFkhqRHeJ9OVlXiGlKmptfllFAJHWFFi2-prJeiqHiuGBz4vFKO4gSjmBG_ACyWCBDy5Da49oGFVGgLy9anUCA8QA8KGBx14y9Uym2538hBjy8oxmrBzk499ry8G8xSieDAhohxi4AbDwEG5HCKqqbyGCAwyDyUS2W69ryonwFxvGi5oPwAzUly9Ef9HKm6E88hzWy-1tDwIU76bypqDxC5E-q3e6F8c8py8pz89Eixu1kwEwGwywr88oS7U6O1hglU7h0XXp40lu1UgaE1a84S0JVE6V0b60jq2m1ow45wdK0Dox0Fw9dwjEcj0pBpQ9z8Si8x65p8jwnFE3Kgqw5CyU9o0piw0TdCo1w8twpA0cHw1e60j60hC588-m0bcw0c1V09YE6F02vU0BO0y80EkEowhE1fpU4-1ewrQ0BU5cE9U1aE2Xw4fw7vClxKu0nS2aaw45yo-0cCw4pa0bUxUw0olo0eeE0DS08Ow5Iw162v807B80Xau040C0qO0cBw192hw','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation','variables': '{"input":{"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1731389053819,749112,4748854339,,","feedback_id":"'+b64enc(f"feedback:{idjob}")+'","feedback_reaction_id":"'+idtype.get(type)+'","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":null,"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+id_page+'","client_mutation_id":"1"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}','server_timestamps': 'true', 'doc_id': '8995964513767096'}
		try:
			self.headers['cookie'] = cookie
			with requests.post(self.url, headers=self.headers, data=data_like) as request_like:
				request_like.raise_for_status()
				if '"errors"' in request_like.text:
					return False
				return True
		except Exception as msg:
			...
		return False
	def Share(self, idfb, hsi, fb1, fb2, lsd, s1, s2, idjob, cookie):
		self.Bypass_CheckPoint(fb1, fb2, cookie)
		data_share = {'av': idfb,'__aaid': '0','__user': idfb,'__a': '1','__req': '19','__hs': '20048.HYP:comet_pkg.2.1..2.1','dpr': '3','__ccg': 'GOOD','__rev': '1018364198','__s': '4mnau3:u0wdg4:gzsrv1','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1vgS3q2ibwyzE2qwJyE24wJwkEkwUx60GE5O0BU2_CxS320qafwwwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1FwIw9i1awkovwRwlE-U2exi4UaEW2G1jwUBwJK14xm3y11xfxmu3W3y261eBx_wHwfC2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHwGwbu','__csr': 'gJ6gngJ97NilTv5ZdjN4nWPkX_Olintjtil_lRRSPcCylX_9lbmHRlenLhAXXiCAnWi9KHHqEy_rAmAQFQ9mlWmHKpppVuOQvgKFbBWyKXAACKVDjGbBgydyQ8ig_UCdgGiEZ2oWqh2k78Jai-aAKFGzECmKu9CByUy2jzGAz8SeGcUOEkyFVE4W4o4Gby8ScyUpBwxKmV9okwn84mayE8EgwnEKbwio34xK5E884a10w9u0JU18o6m3W1bwWw2tE1s80Rq0r-1bwKwlo0nlw09v600KbU8U0D-13w9-0j60py08EwbW1Qw1QK0Yo5a6U0N202K20jh01DR00_4w3qo0apA032jg','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'ComposerStoryCreateMutation','variables': '{"input":{"composer_entry_point":"share_modal","composer_source_surface":"feed_story","composer_type":"share","idempotence_token":"'+str(uuid.uuid4())+'_FEED","source":"WWW","attachments":[{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+idjob+']}"}}],"reshare_original_post":"RESHARE_ORIGINAL_POST","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"is_tracking_encrypted":true,"tracking":[null],"message":{"ranges":[],"text":""},"logging":{"composer_session_id":"'+str(uuid.uuid4())+'"},"navigation_data":{"attribution_id_v2":"CometTahoeRoot.react,comet.videos.tahoe,via_cold_start,1732151849699,995182,2392950137,,"},"event_share_metadata":{"surface":"newsfeed"},"actor_id":"'+idfb+'","client_mutation_id":"1"},"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"gridMediaWidth":null,"groupID":null,"scale":3,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":false,"renderLocation":"homepage_stream","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":true,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":false,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"hashtag":null,"canUserManageOffers":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":true}','server_timestamps': 'true','doc_id': '8832696953514819'}
		try:
			self.headers['cookie'] = cookie
			with requests.post(self.url, headers=self.headers, data=data_share) as request_share:
				request_share.raise_for_status()
				if '"errors"' in request_share.text:
					return False
				return True
		except Exception:...
		return False
				
			
	def Follow(self, id_page, hsi, fb1, fb2, lsd, s1, s2, idjob, cookie):
		data_follow = {'av': id_page,'__aaid': '0','__user': id_page,'__a': '1','__req': '10','__hs': '20042.HYP:comet_pkg.2.1..0.1','dpr': '3','__ccg': 'EXCELLENT','__rev': '1018218440','__s': 'edtzwq:6axw3w:i9k1ze','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG0Z82_CxS320qa2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3qxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHwGwbu','__csr': 'gbQaNA98Afh4Rtn4gBN4ozjONaYSH6h4vv4lkXkOQOmWn9OmBPi-IRnp6AQgYj-GTVlEzp5FWvRjVSijWnjFrGK8HnIDZaUzm8HJah5zdBKQhG-p2lW-iHRKWy-VHKjAymnz5lTAKFAFoWiWAz4-aVeieVaGiHBByFuaCKV9VpKpe7ELy8GXLFtqJ5DDjHCV8CqF9888Ix-6ElDwyBVEcahA8Kq5oKmieBxyEjxCi2GufDzVoaFUGWy8Wmdy9HyEG4EggnyVXzEpCxamqnxem1nCG265pF8ig6iiaKUry84e264lGUS2qEKi3ybGawm825z8mwrF8kBAyQmfU5uUfqG9whUhypoydzojxO1uw4CFacz82nwrokwFwp85K2u0Ao7y0-A0ZA0xoclQ19U5-dm0yk0GU5u6Esw4VwtLCUjOe5K0iXxK0Pd2kewJwGg5K0ME425Ex0iaw1cbw1KC05KE0XiU0iYw0DEw0bIJ07xg1Ro2Sg2iw6ZwbXwa2O044wbWgw5i0Fo2Zg46481ho2oxqu14waME1hE5q0od06Kwso2ew2jum0GU0j0xylw1VV00VZw2q80WW0vqbA807wE08pE3Uw9i5o4Olweq0k6','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUserFollowMutation','variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1731629355728,739771,190055527696468,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+idjob+'","tracking":null,"actor_id":"'+id_page+'","client_mutation_id":"2"},"scale":3}','server_timestamps': 'true','doc_id': '9161999140500267'}
		try:
			self.headers['cookie'] = cookie
			with requests.post(self.url, headers=self.headers, data=data_follow) as request_follow:
				request_follow.raise_for_status()
				if '"errors"' in request_follow.text:
					return False
				return True
		except Exception:...
		return False
	def Comment(self, fb1, fb2, msg, idjob, cookie):
		data_cmt = {'fb_dtsg': fb1, 'jazoest': fb2,'comment_text': msg, 'photo': '(binary)', 'post': 'Bình luận'}
		url = f'https://upload.facebook.com/_mupload_/ufi/mbasic/advanced/?ids&photosrc=advanced_composer_comment&lpwfwef&ft_ent_identifier={idjob}'
		try:
			self.headers['cookie'] = cookie
			request_cmt = requests.post(url, headers=self.headers, data=data_cmt)
			request_cmt.raise_for_status()
			return request_cmt.text
		except Exception:...
		return False
	def ReactCmt(self, id_page, hsi, fb1, fb2, lsd, s1, s2, idjob, type, cookie):
		self.Bypass_CheckPoint(fb1, fb2, cookie)
		idtype = {'LIKE': '1635855486666999', 'LOVE': '1678524932434102', 'CARE': '613557422527858', 'HAHA': '115940658764963', 'WOW': '478547315650144', 'SAD': '908563459236466', 'ANGRY': '444813342392137'}
		data_reactcmt = {'av': id_page,'__aaid': '0','__user': id_page,'__a': '1','__req': '1n','__hs': '20041.HYP:comet_pkg.2.1..0.1','dpr': '2','__ccg': 'EXCELLENT','__rev': '1018190609','__s': 'a6k7tx:bmck3d:3i7pzl','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K360CEboG0x8bo6u3y4o2Gwn82nwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3VwLKq2-azqwaW223908O3216xi4UK2K364UrwFg2fwxyo566k1FwgU4q3Gfw-Kufxa3mUqwjVqwLwHwGwbu','__csr': 'g596MhhRNQn8gvthsjNvikIdnlskBqrV1fOJfYrcYBdWlIIXJaOtbqXYjmL49KTAAhayAu_msxVH8jZaQqVtaqLpprBGjGWQF9By8ljGUGQbACgWapnAEwLABVoOXFeJBCCmmFrhdyUSaKLHz8Ol2VFpk2iqq6A9x91K-i2DyEyiS9UgzF45ES68zAx67UOey9ErGu7Q9yorCx2dwxxm9zErAyU8UebyEqQdzaBABxW5EbU2gyEiAzo8FElzoeUO9G0AHwPw9q14V8jwGyUjxm0zU4h12VoBDg725U1QoaorUK0Sqw4dgaU6Iiqfg523x0cZ057w8a2y1uw6rwqE4q0Do2TwvQ0PE2xWng560XU3PBwpV-7S1swEBU02aiwIgK586y09SU2Yw0bkG0Y82Uc1ew8W1vwkEmwp94UWi1Nw6Pw2pE-2-1kwbC06JE4e9woo2Wxe5t02T87-1ow2hE0oXo0Fy0MA05z9i08V02p2w33sE0i3w18m0s108a0lO0dbw0EIw7cCU3Gw1rlw6ywaS0n-','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation','variables': '{"input":{"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1731557904465,488621,4748854339,,","feedback_id":"'+b64enc(f"feedback:{idjob}")+'","feedback_reaction_id":"'+idtype.get(type)+'","feedback_source":"DEDICATED_COMMENTING_SURFACE","is_tracking_encrypted":true,"tracking":null,"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+id_page+'","client_mutation_id":"2"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}','server_timestamps': 'true','doc_id': '8995964513767096'}
		try:
			self.headers['cookie'] = cookie
			with requests.post(self.url, headers=self.headers, data=data_reactcmt) as request_tcmt:
				request_tcmt.raise_for_status()
				if '"errors"' in request_tcmt.text:
					return False
				return True
		except Exception:...
		return False
	def Page(self, idfb, hsi, fb1, fb2, lsd, s1, s2, idjob, cookie):
		self.Bypass_CheckPoint(fb1, fb2, cookie)
		data_page = {'av': idfb,'__aaid': '0','__user': idfb,'__a': '1','__req': 'c','__hs': '20047.HYP:comet_pkg.2.1..2.1','dpr': '3','__ccg': 'EXCELLENT','__rev': '1018350789','__s': '71eey1:a3fzqh:x7014m','__hsi': hsi,'__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2CE4i5QdwSwAyUco5S3O2Saw8i2S1DwUx60GE3Qwb-q7oc81EEbbwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc60D8vwRwlE-U2exi4UaEW2au0z9obrwh8lwUwgojUlDw-wUwxwjFovUaU3qxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkoqwqo4e4UcEeE-3WVU-4EdrxG1fBG2-2K2G0JU','__csr': 'gpgiv7hIrfaw-hZn2uDOqexv9EGYQZNcDvVatAZ4nFqayiFnqrLldbupcGkQ-ROfAAJqWF9KirBApaG9npeLAAKFrCykqmjh9EGAEWmcAyuF-fGAVuAVKC8mUyVGzKbjGqinGhdat5g99HDz8ymA5KE8UK78KGBGcUS2a8Ku5qyFkbgyawHzo8EiK4V49wJHy84ecwxxO598K69U8o6ei1kyokxW3-cK1AyU421RyEfUO3i0I9o461twp88oaE5G08awc209Fw2no0IZ08a0Q80Ly-0lmuawmE01jLo3EwCg0Xy067E2YwpE0Lu1gwRwYwe-0cYw3Yo0bvU02Cjw','__comet_req': '15','fb_dtsg': fb1,'jazoest': fb2,'lsd': lsd,'__spin_r': s1,'__spin_b': 'trunk','__spin_t': s2,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometProfilePlusLikeMutation','variables': '{"input":{"is_tracking_encrypted":false,"page_id":"'+idjob+'","source":null,"tracking":null,"actor_id":"'+idfb+'","client_mutation_id":"1"},"scale":3}','server_timestamps': 'true','doc_id': '6716077648448761'}
		try:
			self.headers['cookie'] = cookie
			with requests.post(self.url, headers=self.headers, data=data_page) as request_page:
				request_page.raise_for_status()
				if "IS_SUBSCRIBED" in request_page.text:
					return True
				return False
		except Exception:...
		return False
class Unknown:
	def __init__(self):
		self.headers_2fa = {'Host': '2fa.live', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate', 'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': ''}
		self.headers_id_tds = {'Host': 'id.traodoisub.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate', 'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': ''}
	def check_like_idjob(self, arg: str) -> int:
		url = "https://id.traodoisub.com/api.php"
		data_id = {"link": arg}
		try:
			request_id = requests.post(url, headers=self.headers_id_tds, data=data_id)
			request_id.raise_for_status()
			if "success" in request_id.text:
				return 1
			return 0
		except Exception:...
		return 0
			
		
	def Ox2fa_live(self, arg):
		url = f"https://2fa.live/tok/{arg}"
		try:
			self.headers_2fa['cookie'] = '_gcl_au=1.1.730525469.1731465124; _gid=GA1.2.1704517324.1731465125; _ga=GA1.2.504778811.1731465125; _ga_R2SB88WPTD=GS1.1.1731465124.1.1.1731465327.0.0.0'
			request_url = requests.get(url, headers=self.headers_2fa)
			request_url.raise_for_status()
			return request_url.json()
		except Exception as msg:
			...
		return False
		
		