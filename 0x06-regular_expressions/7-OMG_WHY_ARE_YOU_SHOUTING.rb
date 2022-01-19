#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+*[A-Za-z0-9]+)]\s\[to:(\+*[0-9]{11})]\s\[flags:(\-[10]:0:\-[10]:\-?[10]:\-?[10])/).join
