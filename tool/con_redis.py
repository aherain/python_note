import redis
r = redis.Redis(host='10.110.1.97', port=6379, db=0)
a = r.set('foo', 'bar')
print(a)
print(r.get('foo'))

#《趣味数据周刊》：大数据时代，大浪里淘沙，深耕出精品，简洁的图，通俗的文，让热点/真知图文并茂，
# 有趣味不枯燥，不偏激有味道，认知突围，开眼看见新世界，用心体味好生活。
# 每周更新:1-2篇原创文章，【关注】捕获第一眼新鲜
# 历史热文（扫描关注，看一看，瓜不甜，不要钱）：
# 1，电视剧《都挺好》，怎么好？
# 2，看一看：亮眼的趣味图。
# 3，知否，知否，富肥穷瘦？
