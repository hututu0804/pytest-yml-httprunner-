接口自动化测试框架规则
1.必须包含的四个一级关键字  name base_url request validate
2.在request一级关键字下必须包括两个二级关键字：method url
3.如果需要做接口关联，那么必须使用一级关键字： extract，如：
  extract:
        access_token: token
