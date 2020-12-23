import pytest
import yaml
from pythoncode.calculator import Calculator
from test_param_yaml import get_datas

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



    #  使用参数化
    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    # @pytest.mark.parametrize('a', [0, 2, 4, -1])
    # @pytest.mark.parametrize('b,expect', [(0, 0), (2, 0), (3, 1), (-1, 0)])
    # @pytest.mark.parametrize('expect',[0,0,1,-2])
    @pytest.mark.parametrize('a,b,expect',get_datas()[0])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',get_datas()[0])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
