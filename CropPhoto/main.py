from PIL import Image # type: ignore

def split_image(image_path, output_dir):
  """
  将图像平均分割为 4 份

  Args:
    image_path: 输入图像路径
    output_dir: 输出图像保存目录
  """

  # 打开图像
  img = Image.open(image_path)

  # 获取图像尺寸
  width, height = img.size

  # 计算分割点
  half_width, half_height = width // 2, height // 2

  # 分割图像并保存
  img_part1 = img.crop((0, 0, half_width, half_height))
  img_part1.save(f"{output_dir}/part1.jpg")

  img_part2 = img.crop((half_width, 0, width, half_height))
  img_part2.save(f"{output_dir}/part2.jpg")

  img_part3 = img.crop((0, half_height, half_width, height))
  img_part3.save(f"{output_dir}/part3.jpg")

  img_part4 = img.crop((half_width, half_height, width, height))
  img_part4.save(f"{output_dir}/part4.jpg")

# 示例用法
image_path = "D:\Material\Poster\part\part4.jpg"  # 替换为你的图片路径
output_dir = "D:\Material\Poster\part\part4"  # 输出目录

split_image(image_path, output_dir)