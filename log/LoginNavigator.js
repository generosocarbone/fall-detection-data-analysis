import React, {useEffect, useState} from 'react';
import Login from './Login';
import Home from './Home';
import Cards from './Cards';
import CreateAccount from './CreateAccount';
import Register from './Register';
import Profilo from './Profilo';
import Categoria from './Categoria';
import PuntiBeddini from './PuntiBeddini';
import Prodotto from './Prodotto';
import ModificaProfilo from './ModificaProfilo';
import Addresses from './Addresses';
import PasswordRecovery from './PasswordRecovery';
import EmailValidation from './EmailValidation';
import EmailLogin from './EmailLogin';
import Cart from './Cart';
import NewCard from './NewCard';
import NewAddress from './NewAddress';
import HistoricOrderItem from './HistoricOrderItem';
import BeddiniWait from './BeddiniWait';
import OrderHistory from './OrderHistory';
import CreditCardView from './CreditCardView';
import Ordina from './Ordina';
import CheckoutComponent from './CheckoutComponent';
import OrderTypology from './OrderTypology';
import Payments from './Payments';
import {createStackNavigator} from '@react-navigation/stack';
import {connect} from 'react-redux';
import auth from '@react-native-firebase/auth';

////////////////////////
/// login Navigator
////////////////////////
const Stack = createStackNavigator();
const createLoginNavigator = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="Login"
        component={Login}
        options={{
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="Register"
        component={Register}
        options={{
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="CreateAccount"
        component={CreateAccount}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="EmailLogin"
        component={EmailLogin}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="PasswordRecovery"
        component={PasswordRecovery}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="EmailValidation"
        component={EmailValidation}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
    </Stack.Navigator>
  );
};

////////////////////////
/// Main Navigator
////////////////////////
const Main = createStackNavigator();

const createMainNavigator = (navigation) => {
  return (
    <Main.Navigator>
      <Main.Screen
        name="Home"
        component={Home}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Profilo"
        component={Profilo}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="PuntiBeddini"
        component={PuntiBeddini}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Ordina"
        component={Ordina}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Categoria"
        component={Categoria}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Prodotto"
        component={Prodotto}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Cart"
        component={Cart}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="OrderTypology"
        component={OrderTypology}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Delivery"
        component={CheckoutComponent}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Modifica"
        component={ModificaProfilo}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Addresses"
        component={Addresses}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Cards"
        component={Cards}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="Payments"
        component={Payments}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="NewCard"
        component={NewCard}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="NewAddress"
        component={NewAddress}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="OrderHistory"
        component={OrderHistory}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="HistoricOrderItem"
        component={HistoricOrderItem}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
      <Main.Screen
        name="CreditCardView"
        component={CreditCardView}
        options={{
          headerTitle: '',
          headerShown: false,
        }}
      />
    </Main.Navigator>
  );
};

const LoginNavigator = ({dispatch, navigation, profile}) => {
  console.log('LoginNavigator', 'NEW RENDER');
  if (
    profile === undefined ||
    profile === null ||
    Object.entries(profile).length === 0
  ) {
    console.log('LoginNavigato', 'NO PROFILE');
    return createLoginNavigator();
  } else {
    console.log('LoginNavigato', 'PROFILE');
    return createMainNavigator(navigation);
  }
};

const mapStateToProps = ({profile}) => {
  return {
    profile,
  };
};

export default connect(mapStateToProps)(LoginNavigator);
