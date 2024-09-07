from fpdf import FPDF

def images_to_pdf(image_list, output_file='output.pdf'):
  """
  将多张图片整合为一个 A4 尺寸的 PDF

  Args:
    image_list: 图片文件路径列表
    output_file: 输出 PDF 文件名
  """

  pdf = FPDF(format='A4')

  for image_path in image_list:
    pdf.add_page()
    pdf.image(image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # 调整图片大小以适应页面

  pdf.output(output_file)

# 示例用法
image_paths = ['image1.jpg', 'image2.png', 'image3.bmp']
images_to_pdf(image_paths)