import function
from function import *


cls()
class Lib:
	def __init__(self):
		self.FILETOKEN = "C2_TOKENTDS.txt"
		self.FILECOOKIE = "C2_COOKIEFB.txt"
		self.check_file = os.path.exists
		self.status_job_tds = False
		self.doiacc = 4
		self.dem_coin_error = 0
		self.dem_postjob = 0
		self.dem_job_tds = 0
		
		self.tuple_job_error = {"likesieure": 0, "comment": 0, "share": 0, "follow": 0, "reaction": 0, "reactcmt": 0, "page": 0, "group": 0}
	def TDS_PROFILE(self):
		while True:
			if not self.check_file(self.FILETOKEN):
				self.token = input(f"{daucau}{luc}Nhập API Access_Token TDS: {vang}")
				login_tds = API_TDS(self.token).login()
				if not login_tds or 'error' in login_tds:
					print(f"{red}Access Token Không Hợp Lệ! Xin Thử Lại")
					time.sleep(1)
					continue
				self.user = login_tds['data']['user']
				self.xu = login_tds['data']['xu']
				self.xudie = login_tds['data']['xudie']
				with open(self.FILETOKEN, "w") as file:
					file.write(self.token)
				print(f"{lam}Đăng Nhập Thành Công.")
				break
			if self.check_file(self.FILETOKEN):
				with open(self.FILETOKEN, "r") as file:
					self.token = file.read()
				login_tds = API_TDS(self.token).login()
				if not login_tds or 'error' in login_tds:
					print(f"{red}Access Token Không Hợp Lệ! Xin Thử Lại")
					time.sleep(1)
					os.remove(self.FILETOKEN)
					continue
				self.user = login_tds['data']['user']
				self.xu = login_tds['data']['xu']
				self.xudie = login_tds['data']['xudie']
				print(f"{daucau}{luc}Nhập {red}[{vang}1{red}]{luc} Tiếp Tục Tài Khoản TDS: {vang}{self.user}")
				print(f"{daucau}{luc}Nhập {red}[{vang}2{red}]{luc} Để Nhập Access_Token TDS Mới")
				print(f"{daucau}{luc}Nhập {red}[{vang}3{red}]{luc} Thoát Tool")
				choice = input(f"{daucau}{luc}Nhập >>>: {vang}")
				if choice == '1' or choice == '01':
					print(f"{lam}Đăng Nhập Thành Công.")
					break
				elif choice == '2':
					os.remove(self.FILETOKEN)
					print(f"{red}Đã Xóa Access_Token TDS, Vui Lòng Nhập Lại!")
					continue
				elif choice == '3':
					See()
				else:
					print(f"{red}Lựa Chọn Không Hợp Lệ!")
					thanhngang()
					continue
		thanhngang()
		while True:
			if self.check_file(self.FILECOOKIE):
				print(f"{daucau}{luc}Nhập {red}[{vang}1{red}]{luc} Sử Dụng Cookie Facebook Đã Lưu")
				print(f"{daucau}{luc}Nhập {red}[{vang}2{red}]{luc} Nhập Cookie Facebook Mới")
				print(f"{daucau}{luc}Nhập {red}[{vang}3{red}]{luc} Thoát Tool")
				choice2 = input(f"{daucau}{luc}Nhập >>>:{vang} ")
				if choice2 == '1' or choice2 == '01':
					with open(self.FILECOOKIE, "r") as file:
						self.cookie = file.read()
					#break
				elif choice2 == '2':
					os.remove(self.FILECOOKIE)
					print(f"{red}Đã Xóa Cookie Facebook, Vui Lòng Nhập Lại!!!")
					continue
				elif choice2 == '3':
					See()
				else:
					print(f"{red}Lựa Chọn Không Hợp Lệ!")
					thanhngang()
					time.sleep(0.5)
					continue
			if not self.check_file(self.FILECOOKIE):
				self.cookie = input(f"{daucau}{luc}Nhập Cookie Facebook Chứa Page Profile: {vang}").replace(" ", '')
				Getdata = API_FACEBOOK().getdata(self.cookie)
				if Getdata:
					print(f"{tim}Tên FB: {lam}{Getdata[6]}")
					with open(self.FILECOOKIE, "w") as file:
						file.write(self.cookie)
					#break
				else:
					print(f"{red}Cookie Facebook Die, Vui Lòng Nhập Lại!!!")
					time.sleep(0.5)
					continue
			
			Getdata = API_FACEBOOK().getdata(self.cookie)
			if not Getdata:
				print(f"{red}Cookie Facebook Die, Vui Lòng Nhập Lại")
				thanhngang()
				os.remove(self.FILECOOKIE)
				continue
			login()
			GetPro5 = API_FACEBOOK().ShowPro5(Getdata[7], Getdata[4], Getdata[5], Getdata[2], Getdata[3], self.cookie, Getdata[0], Getdata[1])
			if not GetPro5 or len(GetPro5) == 0:
				print(f"{red}Không Tìm Thấy Page Profile!")
				continue
			break		
		thanhngang()
		list1 = list()
		list2 = list()
		dem_page = 0
		print(f"{lam}Tìm Thấy {vang}{len(GetPro5)} {lam}Page Profile From Cookie {vang}{Getdata[6]}")
		thanhngang()
		for x in GetPro5:
			dem_page += 1
			id_page = x['profile']['id']
			name_page = x['profile']['name']
			print(f"{daucau}{red}[{vang}{dem_page}{red}]{luc} Chạy Page: {vang}{name_page} {red}| {luc}ID: {vang}{id_page}")
			list1.append([name_page, id_page])
		print(f"{daucau}{luc}Nhập {red}[{vang}all{red}]{luc} Để Chạy Tất Cả Page")
		print(f"{daucau}{lam}Có Thể Chọn Nhiều Page (Ví Dụ: 1+2+3+4...)")
		while True:
			choice3 = input(f"{daucau}{luc}Nhập >>>:{vang} ").split('+')
			if choice3[0] == 'all':
				list2 = list1
				break
			try:
				for i in list(map(int, choice3)):
					list2.append(list1[i-1])
				break
			except:
				list2 = []
				print(f"{red}Lựa Chọn Không Xác Định!")
				continue
		cls()
		print(f"{daucau}{luc}Tên Tài Khoản: {vang}{self.user}")
		print(f"{daucau}{luc}Xu Hiện Tại: {vang}{self.xu}")
		print(f"{daucau}{luc}Xu Bị Trừ: {vang}{self.xudie}")
		print(f"{daucau}{luc}Số Page Đang Chạy: {vang}{len(list2)}")
		thanhngang()
		listjob1 = ["Like 3", "Comment", "Share", "Follow", "Reaction", "ReactCmt", "Page", "Group"]
		listjob2 = list()
		for x, i in enumerate(listjob1, 1):
			print(f"{daucau}{luc}Nhập {red}[{vang}{x%9}{red}]{luc} Để Chạy Job {i}")
		print(f"{lam}Có Thể Chọn Nhiều Job (Ví dụ: 1234...)")
		while True:
			choice4 = input(f"{daucau}{luc}Nhập >>>:{vang} ")
			if choice4 and choice4.isdigit():
				break
			print(f"{red}Lựa Chọn Không Hợp Lệ!")
			time.sleep(0.5)
			continue
		thanhngang()
		while True:
			dlmin = input(f"{daucau}{luc}Nhập Delay Min: {vang}")
			if dlmin and dlmin.isdigit():
				break
			print(f"{red}Delay Không Hợp Lệ!")
			continue
		while True:
			dlmax = input(f"{daucau}{luc}Nhập Delay Max: {vang}")
			if dlmax and dlmax.isdigit() and int(dlmax) > int(dlmin):
				break
			print(f"{red}Delay Không Hợp Lệ!")
			continue
		ihide = input(f"{daucau}{luc}Tự Động Ẩn ID Facebook (y/n): {vang}")
		listjob3 = ["likesieure", "comment", "share", "follow", "reaction", "reactcmt", "page", "group"]
		set1 = set()
		list3 = list()
		for x, i in enumerate(listjob3, 1):
			if str(x % 9) in choice4 and i not in set1:
				list3.append(i)
				set1.add(i)
		listjob2 = list3
		while True: # while main
			c2 = 0
			if len(list2) == 0:
				list1=[];list2=[]; del dem_page;dem_page=0
				print(f"{red}Đã Xóa Tất Cả Page, Vui Lòng Nhập Lại!!!")
				del self.cookie
				while True:
					self.cookie = input(f"{daucau}{luc}Nhập Cookie Facebook Chứa Page Profile: {vang}").replace(" ", '')
					Getdata = API_FACEBOOK().getdata(self.cookie)
					if Getdata:
						print(f"{tim}Tên FB: {lam}{Getdata[6]}")
						with open(self.FILECOOKIE, "w") as file:
							file.write(self.cookie)
					else:
						print(f"{red}Cookie Facebook Die, Vui Lòng Nhập Lại!!!")
						time.sleep(0.5)
						continue
					Getdata = API_FACEBOOK().getdata(self.cookie)
					if not Getdata:
						print(f"{red}Cookie Facebook Die, Vui Lòng Nhập Lại")
						thanhngang()
						os.remove(self.FILECOOKIE)
						continue
					login()
					GetPro5 = API_FACEBOOK().ShowPro5(Getdata[7], Getdata[4], Getdata[5], Getdata[2], Getdata[3], self.cookie, Getdata[0], Getdata[1])
					if not GetPro5 or len(GetPro5) == 0:
						print(f"{red}Không Tìm Thấy Page Profile!")
						continue
					break
				thanhngang()
				dem_page2 = 0
				print(f"{lam}Tìm Thấy {vang}{len(GetPro5)} {lam}Page Profile From Cookie {vang}{Getdata[6]}")
				thanhngang()
				for x in GetPro5:
					dem_page += 1
					id_page = x['profile']['id']
					name_page = x['profile']['name']
					print(f"{daucau}{red}[{vang}{dem_page}{red}]{luc} Chạy Page: {vang}{name_page} {red}| {luc}ID: {vang}{id_page}")
					list1.append([name_page, id_page])
				print(f"{daucau}{luc}Nhập {red}[{vang}all{red}]{luc} Để Chạy Tất Cả Page")
				print(f"{daucau}{lam}Có Thể Chọn Nhiều Page (Ví Dụ: 1+2+3+4...)")
				while True:
					choice3 = input(f"{daucau}{luc}Nhập >>>:{vang} ").split('+')
					if choice3[0] == 'all':
						list2 = list1
						break
					try:
						for i in list(map(int, choice3)):
							list2.append(list1[i-1])
						break
					except:
						list2 = []
						print(f"{red}Lựa Chọn Không Xác Định!")
						continue
			for page in list2:
				#if c2==1:break 
				c2=0
				if self.cookie.endswith(";"):
					self.cookie2 = f"{self.cookie}i_user={page[1]};"
				else:
					self.cookie2 = f"{self.cookie};i_user={page[1]};"
				cauhinhtds = API_TDS(self.token).config(page[1])
				if not cauhinhtds or 'error' in cauhinhtds:
					print(f"{red}Vui Lòng Thêm ID: {vang}{page[1]}{red} Vào Cấu Hình")
					list2.remove(page)
					break
				else:
					if ihide == 'y':
						Ox1 = Hide_ID(page[1])
					else:
						Ox1 = page[1]
					
					thanhngang()
					print(f"{luc}PAGE: {vang}{page[0]} {red}| {luc}ID: {vang}{Ox1}")
					thanhngang()
				while True:
					if c2 == 1:break
					for self.job in listjob2:
						if c2 == 1:break
						GetJob = API_TDS(self.token).getjob(self.job)
						if not GetJob:
							print(f"{red}Không Get Được Job {vang}{self.job.upper()} ", end="\r")
							time.sleep(5)
							continue
						elif "error" in GetJob.text:
							JSON_GetJob = GetJob.json()
							if JSON_GetJob['error'] == 'Đã đạt giới hạn nhiệm vụ trong ngày hôm nay':
								print(f"{red}PAGE: {page[0]}\nĐã đạt giới hạn nhiệm vụ {self.job.upper()} trong ngày hôm nay\nnvdalam: {JSON_GetJob['nvdalam']} {trang}| {red}time_reset: {str(JSON_GetJob['time_reset'])}      ")
								list2.remove(page);c2=1;break
							else:
								print(f"{red}Đang Get Job {self.job.upper()}, COUNTDOWN {str(JSON_GetJob['countdown'])} ", end="\r")
								time.sleep(15)
								print(" "*50, end="\r")
								continue
						else:
							if self.job == "page" or self.job == "follow":
								JSON_GetJob = GetJob.json()['data']
							else:
								JSON_GetJob = GetJob.json()
							if len(JSON_GetJob) == 0:
								print(f"{red}Hết Job {self.job.upper()}               ", end="\r")
								time.sleep(5)
								print(" "*50, end="\r")
								continue
							else:
								print(f"{lam}Tìm Thấy {vang}{len(JSON_GetJob)} {lam}Job {vang}{self.job.upper()}               ", end="\r")
								for x in JSON_GetJob:
									if self.job == 'likesieure':
										uid = x['id'].split('_')[1]if '_' in x['id']else x['id']
										id = x['id']
										type_job = self.job.upper()
										type = self.job.upper()
										like = API_FACEBOOK().Like(page[1], Getdata[0], Getdata[1], uid, 'LIKE', Getdata[5], Getdata[2], Getdata[3], Getdata[4], self.cookie2)
										if not like:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
									elif self.job == "comment":
										uid = x['id'].split('_')[1]if '_' in x['id']else x['id']
										id = x['id']
										type_job = self.job.upper()
										type = self.job.upper()
										type_msg = x['msg']
										comment = API_FACEBOOK().Comment(Getdata[0], Getdata[1], type_msg, id, self.cookie2)
										if not comment:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
									elif self.job == "share":
										uid = x['id'].split('_')[1]if '_' in x['id']else x['id']
										id = x['id']
										type = self.job.upper()
										type_job = type
										SHARE = API_FACEBOOK().Share(page[1], Getdata[4], Getdata[0], Getdata[1], Getdata[5], Getdata[2], Getdata[3], uid, self.cookie2)
										if not SHARE:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
										
									elif self.job == "follow":
										uid = x['id'].split('_')[1]if '_' in x['id']else x['id']
										id = x['id']
										code = x['code']
										type_job = self.job.upper()
										type = self.job.upper()
										follow = API_FACEBOOK().Follow(page[1], Getdata[4], Getdata[0], Getdata[1], Getdata[5], Getdata[2], Getdata[3], id, self.cookie2)
										if not follow:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
									elif self.job == 'reaction':
										uid = x['id'].split('_')[1]if '_' in x['id']else x['id']
										id = x['id']
										type_job = self.job.upper()
										type = x['type']
										reaction = API_FACEBOOK().Like(page[1], Getdata[0], Getdata[1], uid, type, Getdata[5], Getdata[2], Getdata[3], Getdata[4], self.cookie2)
										if not reaction:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
									elif self.job == "reactcmt":
										uid = x['id'].split('_')[1]if '_' in x['id']else x['id']
										id = x['id']
										type = x['type'] + 'CMT'
										type_job = type
										reactcmt = API_FACEBOOK().ReactCmt(page[1], Getdata[4], Getdata[0], Getdata[1], Getdata[5], Getdata[2], Getdata[3], x['id'], x['type'], self.cookie2)
										if not reactcmt:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
									elif self.job == "page":
										uid = x['id']
										id = x['id']
										code = x['code']
										type = self.job.upper()
										type_job = type
										PAGE = API_FACEBOOK().Page(page[1], Getdata[4], Getdata[0], Getdata[1], Getdata[5], Getdata[2], Getdata[3], id, self.cookie2)
										if not PAGE:
											self.status_job_tds = False
										else:
											self.status_job_tds = True
									COIN = None
									C1 = False
									if self.status_job_tds:
										C1 = True
										if self.job == "follow" or self.job == "page":
											POST_COIN = API_TDS(self.token).postjob(self.job, code)
											self.dem_job_tds += 1
											print(f"{red}[{vang}{self.dem_job_tds}{red}] {lam}{current_time()} {red}[{trang}{POST_COIN['cache']}{luc}/{vang}4{red}] {vang}{type} {tim}{uid} {trang} => {vang}OK")
											if POST_COIN['cache'] != 0:
												if POST_COIN['cache'] % 4 == 0:
													COIN = API_TDS(self.token).getcoin_api_new(self.job, id)
										
										else:
											COIN = API_TDS(self.token).getcoin_api_old(type, id)
										if COIN:
											if "error" in COIN.text:
												OxCoin = COIN.json()
												C1 = False
												if OxCoin['error'] == 'Đã đạt giới hạn nhiệm vụ ngày hôm nay':
													print(f"{red}Đã đạt giới hạn nhiệm vụ ngày hôm nay.       ", end="\r")
													list2.remove(page)
													c2=1;break
													#continue
												self.dem_coin_error += 1
												print(f"{red}GET COIN ERROR {uid}          ", end="\r")
												time.sleep(5)
												continue
											elif 'success' in COIN.text:
												C1 = True
												JS_COIN = COIN.json()
												self.dem_job_tds += 1
												self.tuple_job_error[self.job] = 0
												self.dem_coin_error = 0
												print(f"{red}[{vang}{self.dem_job_tds}{red}] {lam}{current_time()} {vang}{type} {trang}{uid} {lam}{JS_COIN['data']['msg']} {vang}{JS_COIN['data']['xu']}")
												DELAY(random.randrange(int(dlmin), int(dlmax)))
											else:
												print(red, COIN.text)
												time.sleep(5)
										else:
											DELAY(random.randrange(int(dlmin), int(dlmax)))
									else:
										self.tuple_job_error[self.job] += 1
										print(f"{red}{type_job} ERROR {uid}     ", end="\r")
										self.dem_coin_error += 1
										time.sleep(4)
									if self.dem_job_tds != 0:
										if self.dem_job_tds % self.doiacc == 0 and C1:
											c2=1;break
									if self.dem_coin_error != 0 and self.dem_coin_error % 1 == 0:
										checkname1 = API_FACEBOOK().getdata(self.cookie)
										if not checkname1:
											API_FACEBOOK().Bypass_CheckPoint(Getdata[0], Getdata[1], self.cookie)
											print(f"{red}Cookie Tài Khoản {vang}{Getdata[6]} {red}Đã Bị Out!")
											thanhngang()
											list1=[];list2=[];c2=1;break
										else:
											check_bypass = API_FACEBOOK().Bypass_CheckPoint(Getdata[0], Getdata[1], self.cookie)
									
									if self.tuple_job_error[self.job] >= 10:
										checkname2 = API_FACEBOOK().getdata(self.cookie)
										if not checkname2:
											print(f"{red}Cookie Tài Khoản {vang}{Getdata[6]} {red}Đã Bị Out!")
											thanhngang()
											list2=[];c2=1;break
										else:
											print(f"{red}Page {vang}{page[0]}{red} Đã Bị Block Job {self.job.upper()}!        ")
											thanhngang()
											list2.remove(page);c2=1;self.tuple_job_error[self.job]=0;break
											
										
						
											
										
										
										
									
							
					
			
			
	
		
		
#like3, 
				

			
Lib().TDS_PROFILE()

	

#ck = "datr=SyYPZyVRDa_u_X42WyP59Pob; sb=SyYPZxsqDYP-q9oyTglH7Bu8; vpd=v1%3B606x360x2; ps_l=1; ps_n=1; dpr=2.1988937854766846; locale=vi_VN; c_user=61566973418617; fbl_st=101627932%3BT%3A28853379; wl_cbv=v2%3Bclient_version%3A2668%3Btimestamp%3A1731202772; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1731202795698%2C%22v%22%3A1%7D; fr=1hdzUaSKdIHTIfuEv.AWVWM5S--bdvpRGfmeENAsEk3wA.BnMBCo..AAA.0.0.BnMBCo.AWUoAL9JezE; xs=35%3AIMJdiL8VBu1PAQ%3A2%3A1730637608%3A-1%3A-1%3A%3AAcU-fdfcVBHd7_CWvFaajJw2WBFlMwcu6sbVPZSy1A; wd=891x1500; useragent=TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI0LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; "
#ck2 = "datr=SyYPZyVRDa_u_X42WyP59Pob; sb=SyYPZxsqDYP-q9oyTglH7Bu8; vpd=v1%3B606x360x2; ps_l=1; ps_n=1; dpr=2.1988937854766846; c_user=61566973418617; fbl_st=101627932%3BT%3A28853379; wl_cbv=v2%3Bclient_version%3A2668%3Btimestamp%3A1731202772; fr=1hdzUaSKdIHTIfuEv.AWVWM5S--bdvpRGfmeENAsEk3wA.BnMBCo..AAA.0.0.BnMBCo.AWUoAL9JezE; xs=35%3AIMJdiL8VBu1PAQ%3A2%3A1730637608%3A-1%3A-1%3A%3AAcU-fdfcVBHd7_CWvFaajJw2WBFlMwcu6sbVPZSy1A; wd=891x1500; i_user=61567623290181; locale=en_US; useragent=TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI0LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; "
#huhu = API_FACEBOOK()
#abc = huhu.getdata(ck)
#print(abc)
		


