source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "just-the-docs"
gem "jekyll-feed"

# Windows Smart App Control(스마트 앱 제어)이 gem이 로컬 컴파일한 서명 없는 .so를
# 차단하므로, RubyInstaller에 서명된 채로 동봉된 기본 json(2.18.0)을 고정해서 사용.
# 상위 버전을 설치하면 로컬 빌드가 LoadError로 실패함.
gem "json", "2.18.0"

# Windows/JRuby 타임존 픽스
gem "tzinfo-data", platforms: %i[mingw mswin x64_mingw jruby]
gem "wdm", "~> 0.1", platforms: %i[mingw mswin x64_mingw]
