import pytest
import yaml
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print('\n【类计算开始】')
        # 实例化类,生成类的对象
        self.calc = Calculator()
    def teardown_class(self):
        print('\n【类计算结束】')

    def teardowan_class(self):
        print('【计算结束】')

    def setup_method(self):
        print("\n计算开始")

    def teardown_method(self):
        print("\n计算结束")
#     def read_yaml(self):
#         with open('./data.yml') as f:
#             self.yaml_list = yaml.safe_load(f)
#             self.yaml_num = self.yaml_list['datas']
#             print('yaml_num')
#             return [yaml_num]
# T_zcc = TestCalc()
# T_zcc.read_yaml()

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect", [(1, 2, 3), (10000, 10000, 20000)])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(3, 1, 3), (10, 2, 20)])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    # @pytest.mark.parametrize('a', [0, 2, 4, -1])
    # @pytest.mark.parametrize('b,expect', [(0, 0), (2, 0), (3, 1), (-1, 0)])
    # @pytest.mark.parametrize('expect',[0,0,1,-2])
    @pytest.mark.parametrize('a,b,expect',[(0,3,-3),(3,1,2)])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[(4, 2, 2),(3,1,3),(5,6,0)])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
